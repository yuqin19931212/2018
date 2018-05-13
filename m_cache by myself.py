from functools import wraps
import inspect
import time
import datetime

def m_cache(duration):
    def _cache(fn):
        local_cache = {}
        @wraps(fn)
        def wrapper(*args, **kwargs):
            #过期清除
            def clear_expire(cache):
                expire_list = []
                for k, (_, ts) in cache.items():
                    if datetime.datetime.now().timestamp() - ts > duration:
                        expire_list.append(k)
                for k in expire_list:
                    cache.pop(k)
            clear_expire(local_cache)

            def make_key():
                sig = inspect.signature(fn)
                params = sig.parameters
                #位置参数处理
                params_list = list(params.keys())

                key_dict = {}
                for i,v in enumerate(args):
                    k = params_list[i]
                    key_dict[k] = v

                #关键字参数处理
                #for k, v in kwargs.items():
                #    key_dict[k] = v
                key_dict.update(kwargs)

                #缺省值处理
                for k in params_list:
                    if k not in key_dict.keys():
                        key_dict[k] = params[k].default
                return tuple(sorted(key_dict.items()))

            key = make_key() #如何查这个key?

            if key not in local_cache.keys():
                ret = fn(*args, **kwargs)
                local_cache[key] = (ret, datetime.datetime.now().timestamp())

            return local_cache[key]



        return wrapper
    return _cache

def logger(fn):
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        ret = fn(*args, **kwargs)
        delta = (datetime.datetime.now() - start).total_seconds()
        print(delta)
        return ret
    return wrapper

@logger
@m_cache(5)
def add(x, y=5):
    time.sleep(3)
    ret = x + y
    #print(ret)
    return ret

add(4)
add(4, 5)

time.sleep(6)
add(4)
add(4, 5)
