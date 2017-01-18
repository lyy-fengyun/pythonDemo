#!/usr/bin/python
#-*- coding:utf-8 -*-

__auth__='liyayong'
from datetime import datetime
import copy
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class util(object):
    
    def __init__(self):
        '''
        initial the class and prepare some data for the object
        '''
        # 初始化指标数据
        # index为偶数则为所有交易，奇数则表示为充值交易
        self.tmall = [[0] * 24, [0] * 24, [0] * 24, [0] * 24, [0] * 24,
                      [0] * 24, [0] * 24, [0] * 24, [0] * 24, [0] * 24]
        self.all2all = copy.deepcopy(self.tmall)
        self.yjk = copy.deepcopy(self.tmall)
        self.sc = copy.deepcopy(self.tmall)
          
        self.business_line_data = {'tmall':self.tmall, 'all2all':self.all2all, 'sc':self.sc, 'yjk':self.yjk}
        self.bus_order = {0:'tmall',1:'all2all',2:'sc',3:'yjk'}
        
        # 保存分业务线保存所有的字符开头字符串
        self.tmall_tips=[u'所有交易TPS',u'所有交易平均耗时',u'所有交易最大耗时',u'所有交易最小耗时',
                    u'充值交易平均耗时',u'充值交易最大耗时',u'充值交易最小耗时']
        self.all2all_tips=[u'all2all_all_平均TPS',u'all2all_all_最大TPS',u'all2all_all_平均耗时',u'all2all_all_最大耗时',u'all2all_all_最小耗时',
                      u'all2all_充值_平均TPS',u'all2all_充值_最大TPS',u'all2all_充值_平均耗时',u'all2all_充值_最大耗时',u'all2all_充值_最小耗时']
        self.sc_tips=[u'sc_all_平均TPS',u'sc_all_最大TPS',u'sc_all_平均耗时',u'sc_all_最大耗时',u'sc_all_最小耗时',
                      u'sc_充值_平均TPS',u'sc_充值_最大TPS',u'sc_充值_平均耗时',u'sc_充值_最大耗时', u'sc_充值_最小耗时']
        self.yjk_tips=[u'all_平均TPS', u'all_最大TPS',
                       u'all_平均耗时',u'all_最大耗时',u'all_最小耗时',u'chongzhi_平均TPS',
                       u'chongzhi_最大TPS',u'chongzhi_平均耗时',u'chongzhi_最大耗时',u'chongzhi_最小耗时',]
        
        self.tips = {'tmall': self.tmall_tips, 'all2all': self.all2all_tips,
                     'sc': self.sc_tips,'yjk':self.yjk_tips}
        
        self.tmall_index_mapper={0:0,1:2,2:3,3:4,4:7,5:8,6:9,7:10}

        self.pro_code = [100, 200, 210, 220, 230, 240, 250, 270,
                         280, 290, 311, 351, 371, 431, 451, 471,
                         531, 551, 571, 591, 731, 771, 791, 851,
                         871, 891, 898, 931, 951, 971, 991]
        self.pro_tips = {u'分省':1,u'sc_耗时分省':5,u'all2all_耗时分省':3,u'耗时-分省':7}
        self.pro_data = [self.pro_code , [0]*31 ,self.pro_code , [0]*31,self.pro_code,[0]*31,self.pro_code,[0]*31]
        
        self.used_key=[]
        self.used_line=[]
        
        self.used_tips = []
        self.sec_tips = {u'总对总耗时分布':1,u'商城耗时分布':2,u'耗时分布':3}
        self.sec_key = ['1s','2s','3s','5s','10s','<30s','>30s']
        self.sec_data = [[0]*7,[0]*7,[0]*7,[0]*7]
        
        # 文件行号
        self.line_number = 0
        now_day = datetime.now().strftime("%Y%m%d")
        self.yesterday=str(int(now_day)-1)
        #self.yesterday='20170112'
        self.time_list=range(0,24)
        # 得到24小时的日期时间
        for val in self.time_list:
            if val<=9:
                self.time_list[val]= self.yesterday+'0'+str(val)
            else:
                self.time_list[val]= self.yesterday+str(val)

    def is_blank_line(self, line):
        '''
        判断是否是空行或其他类型的无用描述字符
        :param line: one line reading from the file
        :return:
        '''
        if line.startswith('\r\n') or line.startswith('---') or line.startswith('('):
            return True;
        else:
            return False;
    
    def find_the_key(self,line):
        '''
        找到此行数据记录的哪种类型的数据,属于哪个业务线，
        :param line: one line reading from the file
        :return:(bus_line,key) or (None,None)
        '''
        # 先检查上次使用过的bus_line与key
        if len(self.used_key):
            bus_line = self.used_line[-1]
            key = self.used_key[-1]
            #print key
            if line.startswith(key):
                return (bus_line, key)
            
        # 如果没有找到，重新查找
        for bus_line in self.tips.keys():
            for index in  range(len(self.tips[bus_line])):
                key = self.tips[bus_line][index]
                #key =  key.decode('utf-8')
                #print  key.decode("unicode-escape").encode('utf-8')
                
                # print line
                #print key
                if line.startswith(key):
				    # 将没用过的key添加到列表中进行记录
                    if key not in self.used_key:
                        self.used_key.append(key)
                        self.used_line.append(bus_line)
                    #print bus_line,key
                    return (bus_line, key)
        return (None,None)
    
    def to_assign(self,line,bus_line,key):
        '''
        根据line的业务线与key进行赋值
        :param line: one line reading from the file
        :return:None
        '''
        str_lst = line.split()
        #print str_lst
        for my_datetime in self.time_list:
            if str_lst[1] == my_datetime:
                raw = self.time_list.index(my_datetime)
                
                # 10 个指标数据的index
                column = self.tips[bus_line].index(key)
                if bus_line == 'tmall':
                    # 业务线为tmall，重新计算坐标。
                    column = self.tmall_index_mapper[column]
                    if key == u'所有交易TPS':
                        #print (column,raw),(column+1,raw)
                        self.business_line_data[bus_line][column][raw] = str_lst[2]
                        self.business_line_data[bus_line][column+1][raw] = str_lst[3]
                    else:
                        #print (column,raw)
                        self.business_line_data[bus_line][column][raw] = str_lst[2]
                        
                else:
                    # 业务线为其他
                    self.business_line_data[bus_line][column][raw]=str_lst[2]
    
    def print_data(self):
        '''
        write data to csv file
        :return: None
        '''
        file_out = open('final.csv','w')
        
        head = 'time,'+ u'avg_TPS,max_TPS,avg_usedTime,max_usedTime,min_usedTime,' * 8+'\n'
        file_out.write(head)
        
        for raw in range(24):
            #print self.time_list[raw]+',',
            file_out.write(self.time_list[raw]+',')

            for index in range(4):
                for column in range(10):
                    bus_line = self.bus_order[index]
                    #print str(self.business_line_data[bus_line][column][raw])+',',
                    file_out.write(str(self.business_line_data[bus_line][column][raw])+',')
            #print '\n'
            file_out.write('\n')
        
        file_out.write('\n\n')
        
        # print  province data
        for raw in range(31):
            for column in range(8):
                file_out.write(str(self.pro_data[column][raw])+',')
            file_out.write('\n')
        
        
        file_out.write('\n\n')
        # print assumeing data
        for raw in range(7):
            for column in range(4):
                file_out.write(str(self.sec_data[column][raw])+',')
            file_out.write('\n')
            
        file_out.close()
    
    def assign_province(self,line):
        if len(self.used_tips):
            key = self.used_tips[-1]
            if line.startswith(key):
                str_lst = line.split()
                column = self.pro_tips[key]
                raw = self.pro_code.index(int(str_lst[1]))
                self.pro_data[column][raw] = str_lst[2]
                return 0
        
        for key in self.pro_tips.keys():
            if line.startswith(key):
                # 注册最近使用的province tips
                if key not in self.used_tips:
                    self.used_tips.append(key)
                #赋值
                str_lst = line.split()
                column = self.pro_tips[key]
                raw = self.pro_code.index(int(str_lst[1]))
                self.pro_data[column][raw] = str_lst[2]
                return 0
    
    def assign_resume_time(self,line,data):
        '''
        分省耗时，进行判断
        :param line: 文本字符串
        :return:0：成功
        '''
        # 首先对进行存储的关键字进行判断
        if len(self.used_tips):
            key = self.used_tips[-1]
            if line.startswith(key):
                self.toassign_resume(line, key)
                return 0
        
        for key in self.sec_tips.keys():
            # 测试文本开头字符
            if line.startswith(key):
                # 如果匹配到后进行tip注册
                if key in self.used_tips:
                    self.used_tips.append(key)
                # 赋值
                self.toassign_resume(line, key)
                return 0
        tmall_tip = '<1s'
        if line .startswith(tmall_tip):
            # 注册使用过的标识
            if tmall_tip  not in self.used_tips:
                self.used_tips.append(tmall_tip)
            # 得到行号
            num = self.line_number
            #print num
            # 跳过随后的三行文本
            num += 3
            new_line = data[num].strip()
            str_lst = new_line.split()
            for index in range(len(str_lst)):
                colume = 0
                raw = index
                self.sec_data[colume][raw] = str_lst[index]
            new_line = data[num+1].strip()
            self.sec_data[0][-1] = new_line
            return 0
                
        
    def toassign_resume(self,line,key):
        '''
        对分省耗时，进行赋值操作
        :param line:
        :param key: 业务线分省耗时的标识
        :return:
        '''
        str_lst = line.split()
        # 准备进行赋值
        for id in self.sec_key:
            # 判断前一个字符的结尾
            if str_lst[0].endswith(id):
                column = self.sec_tips[key]
                raw = self.sec_key.index(id)
                self.sec_data[column][raw] = str_lst[1]
    
    
    def deal_with_file(self):
        '''
        主要的处理函数
        :return: None
        '''
        
        #file_name = 'tmall_erqi_result_20170112.txt'
        #file_name = 'allSc_yiqi_result_20170111.txt'
        file_name = sys.argv[1]
        file_in = open(file_name,'r')
        
        data = file_in.readlines()
        # 读取文件进行处理
        for line in data:
            self.line_number += 1
            line = line.strip().decode('gbk').encode('utf-8')
            #line = line.strip()
            #print line
            # 判断是否是空行或无用行
            if not self.is_blank_line(line):
                # 找到具体的业务线和指标关键字
                bus_line,key = self.find_the_key(line)
                # 判断是否为空
                if bus_line is not None:
                    self.to_assign(line,bus_line,key)
                
                # 查找分省耗时
                self.assign_province(line)
                
                # 查找分类耗时
                self.assign_resume_time(line,data)
                #if self.sec_tmall_tip:
                #    pass
        # 对tmall业务线的充值tps数据进行赋值
        self.business_line_data['tmall'][5] = self.business_line_data['tmall'][0][:]
        self.business_line_data['tmall'][6] = self.business_line_data['tmall'][1][:]

        # 输出数据
        self.print_data()
        file_in.close()
        
if __name__=='__main__':
    handle = util()
    handle.deal_with_file()
    print 'success: all data is in final.csv'
