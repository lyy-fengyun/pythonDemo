#!/usr/bin/python
#coding=utf-8

#
file = open('demo.txt','w')
file.write('python io demo\nthis is a demo txt')
file.close()


file = open('demo.txt','r')
print file.read(10)
print '====='
print file.readline()

file.close()

# 通过with方法打开文件可以不用处理文件的关闭
with open('demo.txt','r') as f:
    print f.read()
    