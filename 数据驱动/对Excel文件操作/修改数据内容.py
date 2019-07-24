# -*- coding:utf-8 -*-
# Author:D.Gray
import xlrd
from xlutils.copy import copy
work = xlrd.open_workbook("data.xls")
old_work = copy(work)          #copy原文件内容
ws = old_work.get_sheet(0)      #根据索引获取所需修改的sheet页
ws.write(11,2,"无涯社区A")       #对第12行第3列内容修改为“无涯社区”
old_work.save("data.xls")       #保存原文件 或 新建文件保存
