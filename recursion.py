#求n的阶乘—递归
def fac(n):
    if n==1:
        return 1
    return n*fac(n-1)

print(fac(5))

#斐波那契数列—递归
pre = 0
cur = 1
print(pre,cur)
def fib(n,pre=0,cur=1):
    pre,cur = cur,pre+cur
    print(cur,end='')
    if n == 2:
        return
    fib(n-1,pre,cur)

print(fib(5))

data = str(1234)
def revert(x):
    if x == -1:
        return ''
    else:
        return data[x] + revert(x-1)

print(revert(len(data)-1))

def peach(day=9,sum=1):
    sum = 2 * (sum+1)
    day -= 1
    if day == 0:
        return sum
    return peach(day,sum)
print(peach())



