# 觅影词频统计工具

📅 编写日期：2025年2月24日
👨‍💻 作者GitHub：@caspiankexin  
📨 作者邮箱： [联系我](mailto:mirror_flower@outlook.com)  
📢 项目地址：[觅影词频统计工具](https://github.com/caspiankexin/MiYing) 
⏬ 下载地址：[资源下载导航页](https://flowus.cn/cckeker/share/85efac3f-a20d-4f36-b68a-410decf4f6da)
✳️ 转载至：原创

---

## 🌟 工具介绍

觅影词频统计工具是一款专为处理海量文本数据而设计的应用程序，特别适用于对人民日报等大量中文文本资料进行关键词频率分析。

对给定时间范围内，多个关键词在人民日报中的出现次数进行统计，并将统计数据以Excel表格的形式导出。

> 例如：查询“山河秀丽”、“山河破碎”等词汇，在2000-2024年间，分别在人民日报中被提及了多少次。

## 🔥 功能亮点
### 多关键词统计：
能够同时对多个关键词进行词频统计，满足你多样化的分析需求。比如，你可以同时输入 “经济发展”“科技创新”“民生保障” 等关键词，一次性获取它们在人民日报中的出现次数。

### 时间范围设定：
用户可以自由选定年份期限，从起始年份到结束年份，精准统计关键词在每年人民日报中的词频。无论是近五年的热点追踪，还是近十年的趋势分析，都能轻松实现。

### 数据可视化输出：
统计完成后，工具会将数据生成 Excel 表，方便用户进一步处理和分析。清晰的表格形式，让数据一目了然，无论是制作报告还是进行深入研究，都更加便捷。

## 🛠️ 使用场景
| 研究领域 | 应用示例             | 数据价值       |
| ---- | ---------------- | ---------- |
| 舆情分析 | 追踪"碳中和"政策关注度变化曲线 | 发现政策推进关键节点 |
| 文化传播 | 分析传统文化词汇使用频率     | 揭示文化复兴趋势   |
| 经济预测 | 统计行业关键词年度曝光量     | 预判产业发展风向标  |

## 💡编写思路

觅影词频统计工具主要依赖于Python编程语言，结合了`tkinter`库用于构建用户界面，`jieba`库用于中文文本的分词处理，以及`pandas`库来管理数据并导出Excel文件。

1. **文件遍历与分词**：使用os模块遍历文件夹下的所有中文 txt 文件，确保不遗漏任何数据。同时，借助jieba库进行中文分词，将文本内容拆分成一个个词语，为后续的关键词统计打下基础。

2. **时间列表生成**：通过generate_time_list函数，根据用户输入的起始年份和结束年份，生成相应的时间列表。这样，在统计词频时，能够按照年份逐一进行处理，实现精准的时间维度分析。

3. **结果保存与可视化**：利用pandas库将统计结果保存为 Excel 文件，借助tkinter和ttkbootstrap库搭建用户界面，让操作更加简单直观。用户只需要在界面上输入相关参数，点击按钮，就能轻松完成词频统计和数据输出。

## 📖使用方法

使用 “觅影词频统计工具” 非常简单。

**方法一：** 在本文开头的`资源下载导航页`下载`觅影词频统计工具.exe`，直接在Windows系统下使用。

**方法二：** 使用本文最下面的`源代码`，在Python环境下使用。

###  **数据准备**
- 确保文本数据按`年/月/日`层级存储（兼容人民日报爬虫数据格式 ）
- 支持`.txt`格式文件，建议单文件大小<50MB

### **参数设置**  
- 选择根目录（包含年度子文件夹）
- 输入关键词（空格分隔，建议≤20个）
- 设置时间范围（支持1900-2100年）

### **运行结果**
- 点击"开始统计"后，实时显示程序运行信息
- 自动生成`results.xlsx`文件，存储统计的数据

## 🌈 结语

本工具特别适合处理《人民日报》等具有时间连续性的传统媒体结构化文本数据，也可以适用在相似结构的文本分析中，比如分析四六级考试中单词每年的出现频率等，具体使用场景有待发掘。

仅输出了最基础的表格数据，但在数据基础上进行可视化都是更容易的事情，就不着急弄了。但还有一个问题不好解决，就是关键词的的语料库难以找到，没有能力也没有精力去构建一个相关的政治语料库（网上有其他类型的语料库），且不知道该如何划分词语的热度等，都是我无法解决的问题，等之后再看发展吧。


> 注：本工具完全开源，禁止用于商业用途。如需深度定制服务，请邮件联系。

## 👨‍💻 程序源代码

```python
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

        root.attributes("-topmost", True)  # 设置窗口为最上层

        # 添加窗口关闭事件处理，确保点击X按钮也能正确退出

        def on_closing():

            root.quit()  # 退出mainloop

            root.destroy()  # 销毁窗口

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

                image = image.resize((300, 300), Image.LANCZOS)  # 调整图片大小

                photo = ImageTk.PhotoImage(image)

  

                # 创建一个Label组件来显示图片

                image_label = tk.Label(root, image=photo)

                image_label.image = photo  # 保持对图片的引用

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

            root.quit()  # 退出mainloop

            root.destroy()  # 销毁窗口

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

    print("  1. 输入需要分析的人民日报数据文件夹，以2022/2021/2022格式命名年份文件夹")

    print("  2. 输入需要查询的词汇，空格隔开，词汇不能包含特殊字符，输入的词汇数量没有限制")

    print("  3. 输入起始时间点和结束时间点，例如2002和2008，也可以输入2022年01月和2022年10月，但需调整输入的文件夹")

    print("  4. 结果保存为Excel文件，便于后续分析")

    print("  5. 程序开始运行后，需耐心等待！")

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

```
---

如果对您有帮助，感谢打赏！🙇‍♀️🤗🫡

 <img src="https://image.062898.xyz/2025/02/303b772de64207e28de06464675078b4.webp" width="250" />

