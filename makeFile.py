#!/bin/env python
# coding=utf-8
__author__ = 'liyy'

'''
    创建日常总结文件，周计划，周总结，月计划，月总结，整理每月的总结文件,用于每日运行创建文件
'''

import shutil
import os
import datetime
import ConfigParser
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# global var
# dir and file
desktop= u"C:\\Users\\lenovo\\Desktop\\"
back_dir= u"C:\\Users\\lenovo\\Desktop\\03-办公技能提升\\工作记录\\"
conf_file=u"C:\\my_bat_file\\month.ini"

# date
time_fmt='%Y%m%d'
today=datetime.datetime.today()
today_str=today.strftime(time_fmt)
today_weekday=today.weekday()

file_name = u'日常工作总结'
month_plan=[u'月计划',u'月总结']
week_plan=[u'周计划',u'周总结']

passed_day=[]
for day in range(1,5):
    delta = datetime.timedelta(days=day)
    passed_day.append((today-delta).strftime(time_fmt))

def backup_file():
    '''
        备份日常总结文件
    :return: none
    '''
    files = os.listdir(desktop)
    for file in files:
        # 备份日常文件
        for date_str in passed_day:
            if file.endswith(date_str):
                shutil.move(desktop + file, back_dir)
        # # 备件总结文件
        # for plan_str in month_plan:
        #     if file.endswith(plan_str):
        #         shutil.move(desktop + file, back_dir + plan_str)

def make_file(file_name=file_name):
    '''
        创建日常总结文件, 周总结与周计划文件
    '''
    file_today = desktop + file_name + today_str
    # print file_today
    if os.path.exists(file_today):
        pass
    else:
        file_write = open(file_today, 'a')
        string = today_str + u" 工作情况记录"
        # print string
        file_write.write(string)
        file_write.newlines
        file_write.write('1.')
        file_write.newlines
        file_write.write('2.')
        file_write.newlines
        file_write.write('3.')
        file_write.close()
    # 创建周总结文件
    file_today = desktop + today_str
    if (today_weekday == 0):
        file_name = file_today + u"_周计划.txt"
        out = open(file_name, 'w')
        out.write(today_str + " " + u"周计划\n\n")
        out.write("1.\n")
        out.write("2.\n")
        out.write("3.\n")
        out.close()
    elif (today_weekday == 4):
        file_name = file_today + u"_周总结.txt"
        out = open(file_name, 'w')
        out.write(today_str + " " + u"  周总结\n\n")
        out.write("1.\n")
        out.write("2.\n")
        out.write("3.\n")
        out.close()
    # 创建周计划文件
        
def make_month_file():
    '''
        创建月计划与月总结文件
    :return: none
    '''
    if today.month <10:
        last_month = "0"+str(today.month-1)
        this_month = "0"+str(today.month)
    else:
        last_month = str(today.month - 1)
        this_month = str(today.month)
 
    # 创建月计划文件
    file_name = desktop + last_month + u"_月总结.txt"
    out = open(file_name, 'w')
    out.write(last_month + " " + u"月总结\n\n")
    out.write("1.\n")
    out.write("2.\n")
    out.write("3.\n")
    out.close()
    # 创建月总结文件
    file_name = desktop + this_month + u"_月计划.txt"
    out = open(file_name, 'w')
    out.write(this_month + " " + u"月计划\n\n")
    out.write("1.\n")
    out.write("2.\n")
    out.write("3.\n")
    out.close()

def handle_month_file(conf_file_path):
    '''
           整理日常总结文件
       :param conf_file_path:
       :return:
    '''
    cf = ConfigParser.ConfigParser()
    cf.read(conf_file_path)
    yesterday_month = cf.get("month", "yesterday_month")
    today_month = cf.get("month", "today_month")
    
    if yesterday_month.strip() != today_month.strip():
        
        # 创建当月计划与上月总结文件
        make_month_file()
        
        # 整理上月总结文件
        print "整理日常总结文件开始---"
        if yesterday_month <10:
            yesterday_month = "0"+yesterday_month
            
        last_month_day = __gen_month_day()
        files = os.listdir(back_dir)
        for file in files:
            for day in last_month_day:
                #print file
                #print day
                if file.endswith(day):
                    month_dir = back_dir + str(yesterday_month)
                    if not os.path.exists(month_dir):
                        os.mkdir(month_dir)
                    shutil.move(back_dir + file, month_dir)
        print "整理日常总结文件结束---"
        
    cf.set("month", "yesterday_month",today_month)
    cf.set("month", "today_month",today.month)
    cf.write(open(conf_file_path, 'w'))
          
def __gen_month_day():
    '''
    生成上月份的日期
    :return: list last_month_date
    '''
    last_month_date = []
    month = today.month
    
    if (month > 1 and month < 10):
        last_month = month - 1
        last_month = "0"+str(last_month)
    elif (month == 1):
        last_month = 12
    month_days = range(1, 32)
    
    for day_int in month_days:
        if (day_int < 10):
         last_month_date.append(str(last_month) + '0' + str(day_int))
        else:
         last_month_date.append(str(last_month) + str(day_int))
    return last_month_date
    
def main():
    backup_file()
    make_file()
    handle_month_file(conf_file)

if __name__=="__main__":
    main()