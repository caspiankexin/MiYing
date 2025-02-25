# 觅影词频统计工具
一款针对大量文本数据进行词频统计的工具

📅 编写日期：2025年2月24日  
👨‍💻 作者GitHub：@caspiankexin  
📨 作者邮箱： [联系我](mailto:mirror_flower@outlook.com)   
📢 项目地址：[觅影词频统计工具](https://github.com/caspiankexin/MiYing)   
⏬ 下载地址：[http://caspian.ysepan.com/](http://caspian.ysepan.com/)   
✳️ 转载至：原创  

---

## 🌟 工具介绍

觅影词频统计工具是一款专为处理海量文本数据而设计的应用程序，特别适用于对人民日报等大量中文文本资料进行关键词频率分析。通过该工具，用户能够轻松实现对指定年份范围内多个关键词在文本中的出现次数进行统计，并将统计数据以Excel表格的形式导出，方便后续的数据分析和报告生成。

## 🔥 功能亮点
### 多关键词统计：
能够同时对多个关键词进行词频统计，满足你多样化的分析需求。比如，你可以同时输入 “经济发展”“科技创新”“民生保障” 等关键词，一次性获取它们在人民日报中的出现次数。

### 中文语义精准识别：
采用**结巴分词引擎**（jieba）， 复合词识别（如"一带一路"不会被拆解）

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

![](https://cors.zme.ink/http://cdn.idreams.cc/20250225a509a72aea73c06959d2bf91e03eb4ea.webp)

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

---

如果对您有帮助，感谢打赏！🙇‍♀️🤗🫡

 <img src="https://cors.zme.ink/http://cdn.idreams.cc/20250225303b772de64207e28de06464675078b4.webp" width="250" />
