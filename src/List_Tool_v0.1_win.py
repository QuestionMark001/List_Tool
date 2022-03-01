import pandas as pd
import tkinter
from tkinter import filedialog
import os

# 导入EXCEL文件
# 在需要匹配的表格中增加一列匹配字段
print('请选择完整名单所在的.xlsx文件。 Please select the .xlsx file where the Full List is located.\n')

root1 = tkinter.Tk()
root1.withdraw()
filePath1 = filedialog.askopenfilename()
excel_one = pd.read_excel(filePath1,header=None,names=['名称'])

print('请选择可能缺失人员名单所在的.xlsx文件。 Please select the .xlsx file where the MoYu List is located.\n')

root2 = tkinter.Tk()
root2.withdraw()
filePath2 = filedialog.askopenfilename()
excel_two = pd.read_excel(filePath2,header=None,names=['名称','标记'])
# 填充匹配字段值
excel_two['标记'] = '存在'
#匹配两个表格数据
results = pd.merge(excel_one,excel_two,how='left',on='名称')
# 定义没有匹配上的值
results = results .fillna('缺失')
# 按照需求筛选出缺失名单
results = results[(results['标记'] == '缺失')]
# 导出缺失名单
results.to_excel('缺失.xlsx',index=False,columns=['名称'],header=False)

print("完成。 Done.")
os.system("pause") # 请按任意键继续. . .