#!/usr/bin/python
# coding=utf-8
__author__ = 'liyy'
from datetime import datetime
import os
import shutil
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

str = "%Y.%m.%d"
today=datetime.now().strftime(str);
fileSuffix=u"值班情况汇总"

fileName = today+"_"+fileSuffix

print fileName

path=u"C:\\Users\\lenovo\\Desktop"
if (os.path.exists(path+os.sep+fileName+".txt")):
    exit(0)
    
out = open(path+os.sep+fileName+".txt",'w')
out.write(today)
out.write(" ")
out.write(fileSuffix)

out.close()