#!/bin/env python
# coding=utf-8
__author__ = 'liyy'

'''
    readTextFile.py read and display text file
'''

import sys

reload(sys)
sys.setdefaultencoding('utf-8')


# global variable


def readFile():
    filename = raw_input("Enter fileName:\n")
    print
    
    try:
        fobj = open(filename,'r')
    except IOError, e:
        print "*** File open Error: ",e
    else:
        for eachline in fobj:
            print eachline,
        fobj.close()
    
def test():
    '''
        回归测试代码
    '''
    readFile()
    pass


if __name__ == "__main__":
    test()
