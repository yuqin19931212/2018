def show(n):
     tail = " ".join([str(i) for i in range(n, 0, -1)])
     width = len(tail)
     for x in range(1, n):
         print("{:>{}}".format(" ".join([str(j) for j in range(x, 0, -1)]), width))
     print(tail)
show(10)

def showtail(n):
    tail=" ".join([str(i) for i in range(n,0,-1)])
    print(tail)
    for x in range(len(tail)):
        if tail[x] == ' ':
            print(' '*x,tail[x+1:])
showtail(10)

#插入排序**
nums_list=[1,3,2,7,6,9,8,5]
nums=[0]+nums_list #补上哨兵位
length=len(nums)
for i in range(2,length):
    nums[0]=nums[i]
    j =i-1
    if nums[j]>nums[0]:
        while nums[j]>nums[0]:
            nums[j+1]=nums[j]
            j -= 1
            nums[j+1]=nums[0]
print(nums)


#冒泡排序-简单*
nums=[1,3,5,2,4,8,9,7,6]
length=len(nums)
for i in range(length):
    for j in range(length-1-i):
        if nums[j]>nums[j+1]:
            nums[j],nums[j+1]=nums[j+1],nums[j]
print(nums)

#冒泡排序-变形**
num=[1,2,3,4,5,6,7,8,9]
length=len(num)
for i in range(length):
    flag=False
    for j in range(length-1-i):
        if nums[j]>nums[j+1]:
            nums[j],nums[j+1]=nums[j+1],nums[j]
            flag=True
    if not flag:
        break
print(num)

#简单选择排序*
num1=[9,8,7,6,5,4,3,2,1]
length=len(num1)
for i in range(length):
    maxindex=i #给定一个最大值索引
    for j in range(i+1,length):
        if num1[maxindex]<num1[j]:
            maxindex=j #拿到最大值索引

    if i != maxindex: #判断是否需要交换
        num1[i],num1[maxindex]=num1[maxindex],num1[i]
print(num1)

#简单选择排序-变形**
nums=[19,8,7,6,5,4,3,2,1]
length=len(nums)
for i in range(length//2):
    maxindex=i
    minindex=-i-1
    minorigin=minindex

    for j in range(i+1,length-i):
        if nums[maxindex]<nums[j]:
            maxindex=j
        if nums[minindex]>nums[-j-1]:
            minindex=-j-1

    if nums[maxindex]== nums[minindex]: #元素相同
        break

    if i != maxindex:
        nums[i],nums[maxindex]=nums[maxindex],nums[i]
        #如果被交换过，要更新索引
        if i== minindex or i == length + minindex:
            minindex=maxindex

    if minorigin != minindex:
          nums[minorigin],nums[minindex]=nums[minindex],nums[minorigin]
    print(nums)


