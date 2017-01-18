#!/usr/bin/python
#-*- coding:utf-8 -*-

str = '哈哈'

str1 = u'哈哈'

string =  u"哈哈jim"
str2 = {u'哈哈':0}

print str

print str2.keys()[0]

print string.startswith(str1)

test=u'所有交易TPS         2017011023                 25          54'

print test.split()
print test.startswith(u'所有交易TPS')
print test.split()[1]


print 'time,'+ u'平均TPS,最大TPS,平均耗时,最大耗时,最小耗时,' * 8+'\n'
