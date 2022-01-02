import all_get
import xlwt
import time

a,b = all_get.all_main()
wb = xlwt.Workbook()
#创建Workbook
ws = wb.add_sheet('test_sheet')
#创建worksheet
ws.write(0, 0, '标题')
ws.write(0, 1, '内容')

lock = 0
for i in range(len(b)):
    if b[i] != '':
        k = b[i].strip('点击图片进入下一页>>')
        #去除个别内容中多余信息
        ws.write(lock + 1,0,a[i])
        ws.write(lock + 1,1,k)
        lock += 1

wb.save('item.xls')
print('爬取完成!')
print('保存中………')
time.sleep(1.5)
print('存中………')
time.sleep(1.5)
print('中………')
time.sleep(1.5)        
print('保存完成！')
