
def gen():
    print("line1")
    print("ppppp")
    yield 1
    print("line2")
    yield 2
    print("line3")
    return 3

next(gen())
next(gen()) #重新调用
g = gen() #生成了一个新的生成器对象，赋给变量g
print(next(g))
print(next(g))
print(next(g, "end"))

def counter():
    i = 0
    while True:
        i += 1
        yield i

def inc(c):
    return next(c)

c = counter()   #生成一个生成器对象，赋给c
print(inc(c))   #拨同一个对象c，不是重新生成一个对象！！！
print(inc(c))

def counter():
    i = 0
    while True:
        i += 1
        yield i
def inc():
    c = counter()
    return next(c)

print(inc()) #每次重新调用生成器对象
print(inc()) #每次重新调用生成器对象

def inc():
    def counter():
        i = 0
        while True:
            i += 1
            yield i
    c = counter()
    return lambda: next(c)

foo = inc() #拿到lambda函数，赋给foo，并没有调用，注意lambda生成的是匿名函数
print(foo()) #1 调用next（c）函数
print(foo()) #2,形成了闭包，变量c对于lambda函数来说是自由变量


def inc():
    def counter():
        i = 0
        while True:
            i += 1
            yield i
    c = counter()
    def _inc():
        return next(c)
    return _inc

foo = inc() #拿到_inc函数，赋给foo，并没有调用
print(foo()) #1 调用_inc函数,执行next（c），拨一下生成器对象
print(foo())#2,形成了闭包，变量c对于lambda函数来说是自由变量




















