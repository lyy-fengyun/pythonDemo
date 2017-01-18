#!/usr/bin/python
#-*- coding:utf-8 -*-
__auth__='liyayong'

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

my_list=[
['010A00','012A02','012A05','012A08','012A11','012A17',
 '012A18','012A99','013A01','013A04','013A17','013A25',
 '013A26','013A34','014A01','015A03','015A06','015A07'],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
['010A00','0000','[NULL]','012A05','012A08','012A11','012A13',
'012A18','012A99','013A01','013A04','013A17','013A26','013A49','013A34',
'014A01','014A03','015A02','015A03','2998','U99998'],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
['010A00','012A02','012A04','012A05','012A08','012A11','012A13',
'012A17','012A18','012A99','013A01','013A13','013A17','013A25',
'013A34','014A01','014A03','015A02','015A03','015A06','015A07',
'015A08','015A09','012A14','013A18','013A26','013A43'],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]
mapper={'scpay':0, 'bank':2, 'tmall':4}

used_tips=[]
tmall_fenbu_tip = '天猫分步统计'
tmall_fenbu_step = range(1,13)
tmall_fenbu_data = [0]*12

def match():
   #file = "FenLeiXing_result.txt"
   file_name  = sys.argv[1]
   file_in = open(file_name,'r')
   file_out = open('final.csv','a')
   
   # 逐行读取文件
   for line in file_in.readlines():
       # 去掉空格
       line = line.strip()
       #print line
       # 查找此行是否存储有 scpay bank or tmall 字符
       # 首先将文本与最近使用过的tip进行判断，如果不相符，则使用全部tip进行比对查找
       if len(used_tips):
           key = used_tips[-1]
           if line.startswith(key):
               assign_rsp_code(line,key)
               continue
           else:
               pass
       else:
           pass
       
       keys = mapper.keys()
       for key in keys:
           #print key
           if line.startswith(key):
               if key not in used_tips:
                   used_tips.append(key)
               #print line.split()
               assign_rsp_code(line,key)
       
       # tmall 分类统计
       if line.startswith(tmall_fenbu_tip):
           str_lst = line.split()
           for step in tmall_fenbu_step:
               if str_lst[1].endswith(str(step)):
                   tmall_fenbu_data[step -1]=str_lst[2]
                   
   print_lst(file_out)
   print_tmall_step(file_out)
   print 'success: data is in final.csv'
   file_out.close()
   file_in.close()

def  print_tmall_step(file_out):
    tmall = {0:tmall_fenbu_step,1:tmall_fenbu_data}
    file_out.write("tmall step used time,\n")
    for raw in [0,1]:
        for column in range(len(tmall_fenbu_step)):
            #print str(tmall[raw][column]) + ',',
            file_out.write(str(tmall[raw][column]) + ',')
        #print '\n'
        file_out.write('\n')
    
        
# 对不同业务线的交易类型进行赋值
def assign_rsp_code(line,key):
    str_list = line.split()
    column = mapper[key]
    
    # 如果列表中不存在这个交易类型，就添加到列表末尾
    if str_list[1] not in str(my_list[column]):
        my_list[column].append(str_list[1])
        raw = my_list[column].index(str_list[1])
        my_list[column + 1].append(str_list[2])
    else:
        raw = my_list[column].index(str_list[1])
        #print column,raw
        my_list[column+1][raw] = str_list[2]
    
def print_lst(file_out):
    # 将赋值后得到的列表进行输出
    for column in range(6):
        if column == 0:
            file_out.write('scpay,\n')
        elif column ==2:
            file_out.write('bank,\n')
        elif column == 4:
            file_out.write('tmall,\n')
        sub_lst = my_list[column]
        for raw in range(len(sub_lst)):
            file_out.write(str(sub_lst[raw]) + ',')
         #   print str(sub_lst[raw]) + ',',
        file_out.write('\n\n')
        #print '\n'
        
if __name__=="__main__":
   match()
