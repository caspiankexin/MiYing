import os
import jieba
import pandas as pd
import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
import sys
import argparse


def generate_time_list(start_year, end_year):
    """
    生成时间列表。

    :param start_year: 起始年份
    :param end_year: 结束年份
    :return: 时间列表
    """
    return list(range(start_year, end_year + 1))


def count_keywords_in_files(folder_path, keywords, time_list):
    """
    统计文件夹下所有中文txt文件中关键词的出现次数。

    :param folder_path: 文件夹路径
    :param keywords: 要统计的关键词列表
    :param time_list: 时间列表
    :return: 每个时间对应的每个关键词的出现次数列表
    """
    results = {}
    for year in time_list:
        print(f"正在处理 {year} 年的数据...")
        year_folder_path = os.path.join(folder_path, str(year))
        if os.path.isdir(year_folder_path):
            # 初始化关键词计数器
            keyword_counts = {keyword: 0 for keyword in keywords}

            # 使用迭代而不是递归来遍历文件夹和子文件夹
            folders_to_visit = [year_folder_path]
            while folders_to_visit:
                current_path = folders_to_visit.pop()
                for item in os.listdir(current_path):
                    item_path = os.path.join(current_path, item)
                    if os.path.isfile(item_path) and item.endswith('.txt'):
                        with open(item_path, 'r', encoding='utf-8') as file:
                            content = file.read()
                            # 使用jieba进行分词
                            words = jieba.lcut(content)
                            # 统计关键词出现次数
                            for word in words:
                                if word in keyword_counts:
                                    keyword_counts[word] += 1
                    elif os.path.isdir(item_path):
                        folders_to_visit.append(item_path)

            # 将每个时间对应的每个关键词的出现次数列表添加到结果中
            results[year] = [keyword_counts[keyword] for keyword in keywords]
            print(f"{year} 年数据处理完成，关键词统计结果: {keyword_counts}")
        else:
            print(f"警告: {year} 年的文件夹不存在，已跳过")

    return results


def save_results_to_excel(results, keywords, output_file='results.xlsx'):
    """
    将统计结果保存到Excel文件中。

    :param results: 统计结果
    :param keywords: 关键词列表
    :param output_file: 输出Excel文件路径
    """
    df = pd.DataFrame(results, index=keywords)
    df.to_excel(output_file)
    print(f"统计结果已保存到 {output_file}")


def get_resource_path(relative_path):
    """获取资源文件的绝对路径，兼容开发环境和打包后的环境"""
    try:
        if hasattr(sys, '_MEIPASS'):
            path = os.path.join(sys._MEIPASS, relative_path)
            print(f"尝试从_MEIPASS加载资源: {path}")
            return path
        else:
            path = os.path.join(os.path.abspath("."), relative_path)
            print(f"尝试从当前目录加载资源: {path}")
            return path
    except Exception as e:
        print(f"获取资源路径时出错: {e}")
        return relative_path


def show_image_window():
    """显示赞赏码窗口"""
    try:
        # 创建一个简单的Tk窗口用于显示赞赏码
        root = tk.Tk()
        root.title("赞赏码")
        root.attributes("-topmost", True)  # 设置窗口为最上层
        
        # 添加窗口关闭事件处理，确保点击X按钮也能正确退出
        def on_closing():
            root.quit()  # 退出mainloop
            root.destroy()  # 销毁窗口
        
        root.protocol("WM_DELETE_WINDOW", on_closing)

        # 获取屏幕尺寸
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # 设置弹窗尺寸为屏幕的30%
        window_width = int(screen_width * 0.3)
        window_height = int(screen_height * 0.45)

        # 计算弹窗位置，使其居中显示
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)

        # 设置弹窗尺寸和位置
        root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # 尝试加载PNG图片
        try:
            # 检查可能的图片路径
            image_paths = [
                '赞赏码.png',
                './赞赏码.png',
                './images/赞赏码.png',
                '../赞赏码.png'
            ]
            
            image_path = None
            for path in image_paths:
                print(f"检查图片路径: {path}, 存在: {os.path.exists(path)}")
                if os.path.exists(path):
                    image_path = path
                    break
            
            # 如果在常规路径找不到，尝试使用get_resource_path
            if not image_path:
                image_path = get_resource_path('赞赏码.png')
                if not os.path.exists(image_path):
                    image_path = get_resource_path('images/赞赏码.png')
            
            # 如果找到图片，加载它
            if image_path and os.path.exists(image_path):
                print(f"正在加载图片: {image_path}")
                image = Image.open(image_path)
                image = image.resize((300, 300), Image.LANCZOS)  # 调整图片大小
                photo = ImageTk.PhotoImage(image)

                # 创建一个Label组件来显示图片
                image_label = tk.Label(root, image=photo)
                image_label.image = photo  # 保持对图片的引用
                image_label.pack(pady=10)
            else:
                print(f"无法找到图片文件")
                error_label = tk.Label(root, text="无法找到赞赏码图片", font=('Helvetica', 12))
                error_label.pack(pady=10)
                
        except Exception as e:
            # 如果图片加载失败，显示错误信息
            print(f"图片加载失败: {e}")
            error_label = tk.Label(root, text=f"图片加载失败: {e}", font=('Helvetica', 12))
            error_label.pack(pady=10)

        # 创建一个Label组件来显示文字
        text_label = tk.Label(root, text="如果对您有用，感谢进行打赏。", font=('Helvetica', 12))
        text_label.pack(pady=10)
        
        # 添加一个按钮用于关闭窗口
        def close_window():
            print("用户点击关闭按钮")
            root.quit()  # 退出mainloop
            root.destroy()  # 销毁窗口
        
        close_button = tk.Button(root, text="关闭", command=close_window)
        close_button.pack(pady=10)
        
        
        # 运行窗口的事件循环，等待用户关闭
        root.mainloop()
        
        return root
        
    except Exception as e:
        # 如果弹窗创建失败，不影响主程序运行
        print(f"赞赏码窗口创建失败: {e}")
        import traceback
        traceback.print_exc()
        return None


def main():
    # 添加控制台窗口，便于调试
    if hasattr(sys, '_MEIPASS'):
        # 如果是打包后的环境，创建控制台窗口
        import ctypes
        ctypes.windll.kernel32.AllocConsole()
        sys.stdout = open('CONOUT$', 'w', encoding='utf-8')
        sys.stderr = open('CONOUT$', 'w', encoding='utf-8')
        print("程序启动，已创建控制台窗口用于调试")
    
    # 显示程序介绍
    print("="*50)
    print("软件名称：觅影词频统计工具")
    print("软件版本：1.0.0")
    print("作者GitHub：@caspiankexin")
    print("作者邮箱：mirror_flower@outlook.com")
    print("编写时间：2025年9月13日")
    print("版权：免费开源、不得商用")
    print("如果对您有用，感谢进行打赏！！！")
    print("使用方法:")
    print("  1. 输入需要分析的人民日报数据文件夹，以2022/2021/2022格式命名年份文件夹")
    print("  2. 输入需要查询的词汇，空格隔开，词汇不能包含特殊字符，输入的词汇数量没有限制")
    print("  3. 输入起始时间点和结束时间点，例如2002和2008，也可以输入2022年01月和2022年10月，但需调整输入的文件夹")
    print("  4. 结果保存为Excel文件，便于后续分析")
    print("  5. 程序开始运行后，需耐心等待！")
    print("="*50)
    print()

    # 解析命令行参数，仅获取no_reward参数
    parser = argparse.ArgumentParser(description='觅影词频统计工具：一款针对海量文本数据进行词频统计的工具')
    parser.add_argument('--no_reward', action='store_true', help='不显示赞赏码')
    # 仅解析--no_reward参数，忽略其他参数
    args, _ = parser.parse_known_args()
    
    # 在程序最开始显示赞赏码窗口
    reward_window = None
    if not args.no_reward:
        try:
            reward_window = show_image_window()
        except Exception as e:
            print(f"赞赏码窗口创建失败: {e}")
            import traceback
            traceback.print_exc()
    
    # 打印当前工作目录和可能的资源路径
    if hasattr(sys, '_MEIPASS'):
        print(f"PyInstaller _MEIPASS: {sys._MEIPASS}")
        
    # 重新解析所有命令行参数
    parser = argparse.ArgumentParser(description='觅影词频统计工具：一款针对海量文本数据进行词频统计的工具')
    parser.add_argument('--folder', type=str, help='文件夹路径')
    parser.add_argument('--keywords', type=str, help='要统计的关键词，用空格分隔')
    parser.add_argument('--start_year', type=int, help='起始年份')
    parser.add_argument('--end_year', type=int, help='结束年份')
    parser.add_argument('--output', type=str, default='results.xlsx', help='输出Excel文件路径')
    parser.add_argument('--no_reward', action='store_true', help='不显示赞赏码')
    
    args = parser.parse_args()
    
    # 如果没有提供命令行参数，则交互式输入
    folder_path = args.folder
    keywords = args.keywords.split() if args.keywords else None
    start_year = args.start_year
    end_year = args.end_year
    output_file = args.output
    
    if not folder_path:
        print("="*50)
        folder_path = input("请输入需要处理的数据的文件夹的路径: ")
    
    if not keywords:
        keywords_input = input("请输入要统计的关键词，用空格分隔: ")
        keywords = keywords_input.strip().split()
    
    if not start_year:
        start_year = int(input("请输入起始年份: "))
    
    if not end_year:
        end_year = int(input("请输入结束年份: "))
    
    print(f"\n开始统计...")
    print(f"文件夹路径: {folder_path}")
    print(f"关键词: {keywords}")
    print(f"年份范围: {start_year}-{end_year}")
    
    # 生成时间列表
    time_list = generate_time_list(start_year, end_year)
    
    # 统计关键词
    print("\n开始统计关键词出现次数...")
    results = count_keywords_in_files(folder_path, keywords, time_list)
    
    # 保存结果
    print("\n正在保存结果到Excel文件...")
    save_results_to_excel(results, keywords, output_file)
    
    print(f"\n统计完成！结果已保存到 {output_file}")
    
    # 如果没有显示赞赏码窗口，等待用户输入
    if not reward_window:
        input("按Enter键退出...")


if __name__ == "__main__":
    main()