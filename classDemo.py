#!/bin/env python
# coding=utf-8
__author__ = 'liyy'

'''
    
'''

import sys

reload(sys)
sys.setdefaultencoding('utf-8')


# global variable


class FooCLass(object):
    '''
                my first class: Fooclass
    '''
    version = 0.1
    def __init__(self,name='John Doe'):
        '''
            constructor
        :param name: name
        '''
        self.name = name
        print "create a class instance for ", self.name
        
    def showname(self):
        '''
            display instance attribute and class name
        '''
        print 'you name is: ',self.name
        print 'my name is ', self.__class__.__name__
    
    def showver(self):
        '''
            display class version
        :return:
        '''
        print self.version
    def addMe2Me(self,x):
        '''
            applay + operation to argument
        :return:
        '''
        return x+x
def test():
    '''
        回归测试代码
    '''
    foo = FooCLass("jim")
    print foo.addMe2Me('xfjs')
    foo.showname()
    foo.showver()

if __name__ == "__main__":
    test()
