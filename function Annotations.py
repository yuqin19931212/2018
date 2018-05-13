import inspect
from functools import wraps
def check(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print(args, kwargs)
        sig = inspect.signature(fn)
        params = sig.parameters #有序字典
        #for i, (name, param) in enumerate(sig.parameters.items()):
         #   print(i + 1, name, param.annotation, param.kind, param.default)
        #位置参数处理
        param_list = list(params.keys())
        for i, v in enumerate(args):
            k = param_list[i]
            if isinstance(v, params[k].annotation):
                print("==")
            else:
                errstr = "{} {} {}".format(v, 'is not', params[k].annotation)
                print(errstr)
                raise TypeError(errstr)
        #关键字传参处理
        for k, v in kwargs.items():
            if isinstance(v, params[k].annotation):
                print("==")
            else:
                errstr = "{} {} {}".format(v, 'is not', params[k].annotation)
                print(errstr)
                raise TypeError(errstr)

        ret = fn(*args, **kwargs)
        return ret
    return wrapper

@check
def add(x: int,  y: int = 7) -> int:
    return x + y


print(add(4, 8))
#print(add('mag', 'deu'))