#第六周作业
print((lambda x,y:[{x[i]:y[i]}for i in range(2)])(('a','b'),('c','d')))

print((lambda x, y: [{k: v} for k, v in zip(x, y)])(('a', 'b'), ('c', 'd'))) #拉链函数

s1 = "He who has never been to the great wall is not a true man"
a = s1.split()
def revert(x):
    if x == -1:
        return ''
    return a[x] + ' ' + revert(x-1)

print(revert(len(a)-1))









