# -*- coding:utf-8 -*-

import xlrd
import xlwt
import time
from datetime import date,datetime

	
def read_excel(i = 0):
	#open
	wbr = xlrd.open_workbook('/home/pengjialing/test.xls',encoding_override='utf-8')
	wbw = xlwt.Workbook(encoding='utf-8')
	booksheet = wbw.add_sheet('sheet 1',cell_overwrite_ok = True)
	sh = wbr.sheet_by_index(0)
	row = sh.nrows
	col = sh.ncols
	k = 0
	for i in range(row):
		if(sh.cell(i,4).value>'18:30:00'):
			for j in range(col):
				booksheet.write(k,j,sh.cell(i,j).value)
			k = k+1
			print k

	wbw.save('Data.xls')

if __name__ == '__main__':
	read_excel()