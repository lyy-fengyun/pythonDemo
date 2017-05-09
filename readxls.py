# -*- coding: utf-8 -*- 

import  xdrlib ,sys
reload(sys)
sys.setdefaultencoding('utf-8')
import xlrd
import os

filename=u'C:\\Users\\lenovo\\Desktop\\问题汇总\\问题解决模板.xlsx'

def open_excel(file= filename):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception,e:
        print str(e)

#根据索引获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的所以  ，by_index：表的索引
def excel_table_byindex(file= filename,colnameindex=0,by_index=0):
    data = open_excel(file)
    table = data.sheets()[by_index]
    nrows = table.nrows #行数
    ncols = table.ncols #列数
    colnames =  table.row_values(colnameindex) #某一行数据
    list =[]
    for rownum in range(1,nrows):

         row = table.row_values(rownum)
         if row:
             app = {}
             for i in range(len(colnames)):
                app[colnames[i]] = row[i] 
             list.append(app)
    return list

#根据名称获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的所以  ，by_name：Sheet1名称
def excel_table_byname(file= filename,colnameindex=0,by_name=u'Sheet1'):
    data = open_excel(file)
    table = data.sheet_by_name(by_name)
    nrows = table.nrows #行数 
    colnames =  table.row_values(colnameindex) #某一行数据 
    list =[]
    for rownum in range(1,nrows):
         row = table.row_values(rownum)
         if row:
             app = {}
             for i in range(len(colnames)):
                app[colnames[i]] = row[i]
             list.append(app)
    return list

# 将内容写到文本
def wirte_string_to_file(string,filename):
    dir = 'files'
    if not os.path.exists(dir):
        os.mkdir(dir)
    file = open(dir+os.sep+filename+'.txt','w')
    file.write(string)
    print "write  to " +filename

def getString(row_string):
    head_list = [u"问题描述", u"涉及主机或数据库", u"解决步骤", u"问题原因"]
    string=""
    for key in head_list:
        string = string + key+': '+os.linesep+row_string.get(key)+os.linesep+os.linesep
    return string

def gen_file():
    '''
        生成文件
    :return:
    '''
    # 清除已有文件
    file_dir = "files"
    files = os.listdir(file_dir)
    for file in files:
        txt_file=file_dir+os.sep+file
        os.remove(txt_file)
    
    # 生成文件
    tables = excel_table_byname()
    for row in tables:
        filename = str(row.get(u"序号")) + ' ' + row.get(u"问题描述")
        filename = filename.replace('\n', '').replace(',', '').replace(':', '')[0:10]
        string = getString(row)
        wirte_string_to_file(string, filename)

def gen_list():
    '''
        生成索引列表
    :return:
    '''
    # 生成文件
    tables = excel_table_byname()
    list_file=u"问题描述列表.txt"
    file = open(list_file, "w")
    for row in tables:
        filename = str(row.get(u"序号")) + ' ' + row.get(u"问题描述")
        file.write(filename+"\n")

    file.close()
            
    


def main():
    gen_file()
    gen_list()
  
  

if __name__=="__main__":
    main()