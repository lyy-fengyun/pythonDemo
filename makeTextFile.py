#!/bin/env python
# coding=utf-8
__author__ = 'liyy'

'''
    makeTextFile.py create text file
'''

import sys
import os

reload(sys)
sys.setdefaultencoding('utf-8')


# global variable
ls = os.linesep

def getFileName(fname):
    while True:
        if os.path.exists(fname):
            print "ERROR: '%s' already exists." % fname
        else:
            break
    
    all = []
    
    print "\nEnter lines('.' by itself to quit)\n"
    
    while True:
        entry = raw_input("> ")
        if entry =='.':
            break
        else:
            all.append(entry)
    fobj = open(fname,'w')
    fobj.writelines(['%s%s' % (x,ls) for x in all])
    fobj.close()
    print "DONE."
        




def test():
    '''
        回归测试代码
    '''
    getFileName("filetest")


if __name__ == "__main__":
    test()
