#!/usr/bin/env python

import multiprocessing
import time
def func(name):
  time.sleep(2)
  return 'start process\n'+name.upper()

if __name__ == '__main__':
  results = []
  p = multiprocessing.Pool(5)
  for i in range(7):
    res = p.apply_async(func,args=('kel',))
    results.append(res)
  for i in results:
    print i.get()