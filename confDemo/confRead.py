#!/bin/env python
# coding=utf-8
__author__ = 'liyy'

import sys
import ConfigParser


reload(sys)
sys.setdefaultencoding('utf-8')
'''
    read conf and set conf content
'''

conf_file = "conf.ini"
def handConf(conf_file):
    cf = ConfigParser.ConfigParser()
    cf.read(conf_file)
    yesterday_month = cf.get("month","yesterday_month")
    today_month = cf.get("month","today_month")
    
    print yesterday_month
    print today_month
    print type(yesterday_month)
    
    cf.set("month", "yesterday_month",today_month)
    cf.set("month", "today_month","6")
    yesterday_month = cf.get("month", "yesterday_month")
    today_month = cf.get("month", "today_month")

    
    print yesterday_month
    print today_month
    print type(yesterday_month)
    cf.write(open(conf_file,'w'))
    
if __name__=="__main__":
    handConf(conf_file)