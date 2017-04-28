#!/usr/bin/python
# coding=utf-8
__author__ = 'liyy'
from datetime import datetime
import os
import shutil
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class file_maker(object):
    '''
        创建空白文件，并将昨天写的记录文件转移备件
    '''
    
    def __init__(self):
        self.file_name = u'日常工作总结'
        now = datetime.now()
        self.today = datetime.strftime(now, '%Y%m%d')
        self.backup_date=[]
        # 备份四天前的文件
        for i in [1,2,3,4]:
            my_date=str(int(self.today) - i)
            self.backup_date.append(my_date)
        self.file_path = u"C:\\Users\\lenovo\\Desktop"
        self.backup_path = u"C:\\Users\\lenovo\\Desktop\\03-办公技能提升\\工作记录"
        self.summary="周总结"
        self.plan="周计划"
    
    def backup(self):
        #print self.yesterday
        for my_date in self.backup_date:
            filename_to_backup = self.file_name + my_date
            file_need_to_backup = self.file_path + os.sep + filename_to_backup
            #print file_need_to_backup
            #print os.path.exists(file_need_to_backup)
            #print os.path.exists(self.backup_path)
            if os.path.exists(file_need_to_backup):
                if not os.path.exists(self.backup_path):
                    os.mkdir(self.backup_path)
                shutil.move(file_need_to_backup, self.backup_path)
            # files = os.listdir(self.file_path)
            # for file in files:
            #     if file.
            
        return 0
    
    def makefile(self):
        file_today = self.file_path + os.sep+self.file_name+self.today
        #print file_today
        if  os.path.exists(file_today):
            pass
        else:
            file_write=open(file_today, 'a')
            string=self.today+u" 工作情况记录"
            #print string
            file_write.write(string)
            file_write.close()
            #print "file maked"
        return 0
    
    def touch_plan_file(self):
        file_today = self.file_path + os.sep  + self.today
        print datetime.now().weekday()
        if (datetime.now().weekday() == 0):
            file_name = file_today+u"_周计划.txt"
            out = open(file_name,'w')
            out.write(self.today+" "+u"周计划\n\n")
            out.write("1.\n")
            out.write("2.\n")
            out.write("3.\n")
        elif(datetime.now().weekday() == 4):
            file_name = file_today + u"_周总结.txt"
            out = open(file_name, 'w')
            out.write(self.today + " " + u"  周总结\n\n")
            out.write("1.\n")
            out.write("2.\n")
            out.write("3.\n")
            
    
if __name__ == "__main__":
    touch = file_maker()
    touch.backup()
    touch.makefile()
    touch.touch_plan_file()
    