# 
# @Author: QinYong by 2017/6/26
# @Desc: 

from contextlib import contextmanager

@contextmanager
def with_run():
    print ('in __enter__ ')
    yield 'think'
    print ('in __exist__')

with with_run() as value:
    print ("I'm %s" % value)

if __name__ == '__main__':
    pass
