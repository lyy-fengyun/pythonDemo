#!/usr/bin/python                        #  1
#coding= utf-8                           #  2
                                         #  3
import fileinput                         #  4
for line in fileinput.inputinplace=True): #  5
	line =line.rstrip)                     #  6
	num = fileinput.lineno)                #  7
	print '%-40s # %2i' %line, num)        #  8
