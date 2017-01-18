

import time
import uuid
import functools
import threading
import logging

# global engin object
engin = None

def nex_id(t=None):
    """
    生成一个唯一id, 当前时间+随机数
    """
    if t is None:
        t = time.time()
        return '%015d%s000' %(int(t*1000), uuid.uuid4().hex)

def _profiling(start,sql=''):
    '''
    用于剖析sql的执行时间
    '''
    t = time.time() - start
    if t > 0.1
        logging.warning('[PROFILING] [DB] %s：%s' % (t,sql))
    else:
        logging.info('[PROFILING] [DB] %s：%s' % (t,sql))

def create_engine(user,passwd, database, host='127.0.0.1',port=3306,**kw):
    '''
    db模型的核心函数，用于连接数据库，生成全局对象engine
    engin对象持有数据库连接
    '''