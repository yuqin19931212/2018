def copy_properties(src, dst):
    dst.__name__ = src.__name__
    dst.__doc__ = src.__doc__
def logger(fn):
    def wrapper(*args, **kwargs): #可变参数
        print('before')
        ret = fn(*args, **kwargs) #参数解构
        print('after')
        return ret

    copy_properties(fn, wrapper)  # 此时fn已经有了，_logger也定义过了。
    return wrapper #不能放在此句之后，此时装饰器已经执行，add函数已经改变，没有意义！！！

@logger #add1 = logger(add1) #logger里面的行参add1形成了闭包，不会被清除掉，是外层函数的本地变量，对_looger来说是自由变量
def add(x, y):
    return x+y
print(add(4, 5))#add1相当于内层函数的引用_logger

print(add.__name__, add.__doc__, sep='\n')


def copy_properties(src):
    def _copy(dst):
        dst.__name__ = src.__name__
        dst.__doc__ = src.__doc__
        return dst
    return _copy

def looger(fn):
    @copy_properties(fn)  #@_copy ==>_copy =  _copy(wrapper)  带参装饰器
    def wrapper(*args, **kwargs):
        '''this is a wrapper'''
        print('before')
        ret = fn(*args, **kwargs)
        print('after')
        return ret

    return wrapper #不能放在此句之后，此时装饰器已经执行，add函数已经改变，没有意义！！！

@looger #add = logger(add)
def add(x, y):
    '''
    This is a function
    return int
    '''
    return x + y

print(add.__name__, add.__doc__, sep='\n')



import datetime
import time

def copy_properties(src):
    def wrapper(dst):
        dst.__name__ = src.__name__
        dst.__doc__ = src.__doc__
        return dst
    return wrapper

import functools
def logger(t):
    def _logger(fn):
        #@copy_properties(fn)
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
             start = datetime.datetime.now()
             ret = fn(*args, **kwargs)
             duration = (datetime.datetime.now() - start).total_seconds()
             if duration > t:
                print("function {} took {}s".format(fn.__name__, duration))
             return ret
        #functools.update_wrapper(wrapper, fn)
        return wrapper
    return _logger

@logger(3) #add = logger(add)
def add(x, y):
    '''
    this is a fuction
    call add
    '''
    time.sleep(3)
    return x+y

print(add(4, 6))
#print(add.__name__, add.__doc__, sep='\n')














