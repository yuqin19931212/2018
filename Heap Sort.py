import math

origin = [0, 30, 20, 80, 40, 50, 10, 60, 70, 90]
total = len(origin) - 1

def print_tree(array):
    length = len(array) - 1
    depth = math.ceil(math.log2(len(array)))

    index = 1
    width = 2 ** depth - 1
    for i in range(depth):
        for j in range(2 ** i):
            print("{:^{}}".format(array[index], width), end=' ')
            index += 1
            if index > length:
                break
        width = width // 2
        print()

#print_tree(origin)

#单个结点的调整

def heap_adjust(n, i ,array:list):
    while 2 * i <= n:
        lchild_index = 2 * i
        max_child_index = lchild_index
        if n > lchild_index and array[lchild_index] < array[lchild_index + 1]:#有右孩子，且右孩子的值大于左孩子的值
            max_child_index = lchild_index + 1
        #与子树的根结点比较
        if array[max_child_index] > array[i]:
            array[i], array[max_child_index] = array[max_child_index], array[i]
            i = max_child_index
        else:
            break
    #print_tree(array)

#heap_adjust(total, total // 2, origin)
#print(origin)

#构建大顶堆
def max_heap(total, array:list):
    for i in range(total // 2, 0, -1):
        heap_adjust(total, i, array)
    return array
max_heap(total, origin)
#print_tree(max_heap(total, origin))

#排序
def sort(total, array:list):
    while total > 1:
        array[1], array[total] = array[total], array[1]
        total -= 1
        if total == 2 and array[total] >= array[total - 1]:
            break
        heap_adjust(total, 1, array)
    return array

print_tree(sort(total, origin))

