# coding:utf-8

import xlrd
exl = xlrd.open_workbook(r'C:\Users\imade\Desktop\test.xlsx')
print exl,type(exl)
print exl.sheet_names()
sheet1 = exl.sheets()[0]
# print exl.sheet_by_index(1)
# print exl.sheet_by_name('Sheet2')
print sheet1.nrows,sheet1.ncols
print sheet1.row_values(1)
print sheet1.col_values(0)
# 第二行，第1列的值，4种方法
print sheet1.cell(1,0).value
print sheet1.cell_value(1,0)
print sheet1.row(1)[0].value
print sheet1.col(0)[1].value