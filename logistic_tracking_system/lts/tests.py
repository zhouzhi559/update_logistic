from django.test import TestCase
import datetime
import os
# Create your tests here.
# s = "123456"
# d = "123,456,678"
#
# st = s.split(",")
# dr = d.split(",")
#
# print(len(st))
#
# print("dr-----", len(dr))
# print(dr)
#
# print(st)

#
# class Page:
#     def __init__(self, currentPage, pageSize, rec_list):
#         """
#
#         :param totalPage: 总页数
#         :param recordCount: 总记录数
#         :param currentPage: 当前页
#         :param pageSize:每页的数量
#         """
#
#         self.currentPage = currentPage
#         self.pageSize = pageSize
#         self.recordCount = len(rec_list)
#         self.rec_list = rec_list
#         self.totalPage, remainder = divmod(self.recordCount, self.pageSize)
#         if remainder:
#             self.totalPage += 1
#         self.set_datas()
#
#     def set_datas(self):
#         start_index = (self.currentPage - 1) * self.pageSize
#         end_index = self.currentPage * self.pageSize
#         self.datas = self.rec_list[start_index:end_index]
#         del self.rec_list
#
#     def get_str_json(self):
#         # return str(self.__dict__).replace("'", "\"")
#         return str(self.__dict__)
#
#
# if __name__ == '__main__':
#     rec_list = [123, 456, 768, 111, 132, 65465, 999, 7887, 898,87]
#     page = Page(1, 3, rec_list)
#     print(page.get_str_json())


# from django.core.paginator import Paginator
# goods_list = []  #定义一个商品列表
# for x in range(1,10): #一共9个商品   列表取头不取尾
#     goods_list.append('Goods' + str(x))
#     paginator = Paginator(goods_list,3)
#
#     print(paginator)

#
# list1 = (('Im_User_1', '0207', 'test', 'test', '001', '在职', 1),)
# s = list1[0][0]
#
# print(s)

# s = datetime.datetime.now().strftime("%Y-%m-%d")
#
# print(s)



# rec_list = [123, 456, 768, 111, 132, 65465, 999, 7887, 898,87]
#
# #  前端传入（4，2）  4页  每页2个数据
#
# data1 = [[123, 456], [768, 111], [132, 65465], [999, 7887]]
#
# data2 = [[123, 456], [768, 111], [132, 65465], [999, 7887, 898, 87]]
#
# s = "product_transit_dsf_hf"
# print(s[16:])
#
# s = []
#
# if s:
#     print("ok")
# else:
#     print("ooooooo")

# s = "product_transit_cmvdk_c"
# s = s[16:]
# print(s)


# a = [{"name": "牛郎", "age": 12}, {"name": "许仙", "age": 20}, {"name": "董永", "age": 18}]
#
# a.sort(key=lambda x:(x['age']), reverse=True)
# print(a)
# str_all = """
# 555555,
# 666666
# """
# with open("text1.txt", "w+", encoding="utf-8") as f:
#     f.seek(0)
#     f.write(str_all)


from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication
from PyQt5.QtPrintSupport import QPrinter

#
# 将要打印的东西生成pdf
#
# 908204694@qq.com

a = QApplication([])
document = QTextDocument()
html = """
<head>
<title>Report</title>
<style>
</style>
</head>
<body>
<table width="100%">
<tr>
<td><img src="{}" width="30"></td>
<td><h1>REPORT汉字试试哈</h1></td>
</tr>
</table>
<hr>
<p align=right><img src="{}" width="300"></p>
<p align=right>Sample</p>
</body>
""".format('./aa.png', './bb.png')

document.setHtml(html)
printer = QPrinter()
printer.setResolution(96)
printer.setPageSize(QPrinter.Letter)
printer.setOutputFormat(QPrinter.PdfFormat)
printer.setOutputFileName("test.pdf")

# 设置纸张的边距
printer.setPageMargins(12, 16, 12, 20, QPrinter.Millimeter)
document.setPageSize(QSizeF(printer.pageRect().size()))
print(document.pageSize(), printer.resolution(), printer.pageRect())
document.print_(printer)









