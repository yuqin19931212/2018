#写一个sorted函数 -- method #1
lst = [1, 3, 2, 4, 5, 8, 7, 9, 6]
def sort(lst, reverse= False):
    ret = []
    for x in lst:
        ret.append(x)
    length = len(ret)

    def inc():
        return ret[j] > ret[j + 1] if not reverse else ret[j] < ret[j + 1]

    for i in range(length):
        flag = False
        for j in range(length - 1 - i):
            if inc():
                ret[j], ret[j+1] = ret[j+1], ret[j]
                flag = True
        if not flag:
            break
    return ret

print(sort(lst,reverse=True))

def sort(iterable,key= None):
    ret = []
    if key is None:
        key = lambda a, b: a > b
    for x in iterable:
        for i, y in enumerate(ret):
            if key(x, y):
                ret.insert(i, x)
                break
        else:
            ret.append(x)
    return ret

print(sort(lst))