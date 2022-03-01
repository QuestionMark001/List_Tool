<!--
 * @Author: QuestionMark001
 * @Date: 2022-03-01 19:46:21
 * @LastEditors: QuestionMark001
 * @LastEditTime: 2022-03-01 21:39:34
 * @FilePath: \LocalProjects\List_Tool\README.md
 * @Description: 
 * 
 * Copyright (c) 2022 by QuestionMark001, All Rights Reserved. 
-->
# List_Tool  

___  

## 这是一个基于Python的Excel名单对比工具  

### Windows操作系统  

**本项目基于 `Python` 编写，需要安装并配置好 `Python`，使用源代码前请使用以下 `pip` 命令安装 `pandas` 模块。**  

```powershell
pip install pandas
```  

### 🍕如何使用  

#### 🎉使用例  

![使用例](img/使用例.gif "使用例")  

**🎈 本工具会分两次提醒你打开文件，第一次请打开完整名单，第二次请打开要检查的名单，请保证 *人员姓名均在第一张工作表的 A列* ；缺失的人员姓名将以 `缺失.xlsx` 生成。**  

**假设**现有两份Excel表格，分别是 `1.xlsx` 和 `2.xlsx` ，其中 `1.xlsx` 是 *`完整名单`* ，`2.xlsx` 是可能有人员缺失的名单，且两份名单之间的排序是不同的（也可以相同）。  

___  

❗**注意：**  
请保证两份Excel表格除人员姓名之外 **无其他数据** ,且**人员姓名均在第一张工作表的A列**，则可以使用本工具进行对比。  

**例如：**  

***完整名单：***  

![完整名单](img/完整名单.png "1.xlsx")  

***可能有缺失的名单：***  

![完整名单](img/可能有缺失的名单.png "2.xlsx")  
