#!/usr/bin/env python

import multiprocessing

class MyProcess(multiprocessing.Process):
    def __init__(self,name,func,args):
        super(MyProcess,self).__init__()
        self.name = name
        self.func = func
        self.args = args
        self.res = ''

    def run(self):
        self.res =  self.func(*self.args)
def func(name,q):
    q.put('start process...')
    q.put(name.upper())

if __name__=='__main__':
    processes = []
    q = multiprocessing.Queue()
    for i in range(4):
        p = MyProcess('process',func,('kel',q))
        processes.append(p)
    for i in processes:
        i.start()
    for i in processes:
        i.join()
    while q.qsize() > 0:
        print q.get()
