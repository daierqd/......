#管理员模式 操作题库
import xlrd
import xlwt
import time
from xlutils.copy import copy
import os

def duiying(memberd):
    workbook = xlrd.open_workbook('E:/python/保存的代码/知识健康系统大作业/resources_get/item.xls', 'r')
    Data = workbook.sheets()[0]
    row = Data.col_values(0)
    row.pop(0)
    k = row[memberd]
    return k

def look_all_title():
    workbook = xlrd.open_workbook('E:/python/保存的代码/知识健康系统大作业/resources_get/item.xls','r')
    Data = workbook.sheets()[0]
    row = Data.col_values(0)            #取出第一列
    row.pop(0)
    return row
                                    # return type == list  ['a','b','c'] :example
def look_all_count():
    workbook = xlrd.open_workbook('E:/python/保存的代码/知识健康系统大作业/resources_get/item.xls','r')
    Data = workbook.sheets()[0]
    row = Data.col_values(1)            #取出第二列
    row.pop(0)
    return row
                                    # return type == list  ['a','b','c'] :example

def search_title(title):
#输出结果字符串返回题目字符串
    workbook = xlrd.open_workbook('E:/python/保存的代码/知识健康系统大作业/resources_get/item.xls','r')
    Data = workbook.sheets()[0]
    row = Data.col_values(1)            #取出二列
    count = 0
    for i in row:
        if row[count] == title:
            row_1 = Data.col_values(0)
            return row_1[count]     #return type == str
        count += 1
    if title not in row:
        return '题库标题不存在，请更新题库!'

def search(title):
#输出题目字符串返回结果字符串
    workbook = xlrd.open_workbook('E:/python/保存的代码/知识健康系统大作业/resources_get/item.xls','r')
    Data = workbook.sheets()[0]
    row = Data.col_values(0)            #取出第一列
    count = 0
    for i in row:
        if row[count] == title:
            row_1 = Data.col_values(1)
            return row_1[count]     #return type == str
        count += 1
    if title not in row:
        return '题库标题不存在，请更新题库!'

def add(title,count):
#添加标题和内容    
    workbook = xlrd.open_workbook('E:/python/保存的代码/知识健康系统大作业/resources_get/item.xls','r')
    Data = workbook.sheets()[0]
    row = Data.col_values(0)
    line = len(row)
    new_workbook = copy(workbook)  # 将xlrd对象拷贝转化为xlwt对象
    new_worksheet = new_workbook.get_sheet(0)  # 获取转化后工作簿中的第一个表格
    new_worksheet.write(line,0,title)
    new_worksheet.write(line,1,count)
    new_workbook.save('E:/python/保存的代码/知识健康系统大作业/resources_get/item.xls')

def delete(cols):
    workbook = xlrd.open_workbook('E:/python/保存的代码/知识健康系统大作业/resources_get/item.xls')
    Data = workbook.sheets()[0]
    row = Data.col_values(0)
    if cols not in row:
        return '题库标题不存在，请更新题库!'
    counts = 0
    for i in row:
        if row[counts] == cols:
            a1 = Data.col_values(0)
            a1.pop(counts)
            a2 = Data.col_values(1)
            a2.pop(counts)
            os.remove('E:/python/保存的代码/知识健康系统大作业/resources_get/item.xls')
            wb = xlwt.Workbook()
            ws = wb.add_sheet('test_sheet')
            for j in range(len(a1)):
                ws.write(j,0,a1[j])
                ws.write(j,1,a2[j])
            wb.save('E:/python/保存的代码/知识健康系统大作业/resources_get/item.xls')
        counts += 1
            
    
