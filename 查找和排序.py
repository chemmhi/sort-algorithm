# Author: Chenchen

import random
# 二分法查找
def bin_search(data_li, value):
  low = 0
  high = len(data_li) - 1
  while low <= high:
    mid = (low + high) // 2
    if data_li[mid] == value:
      return mid
    elif data_li[mid] >value:
      high = mid-1
    else:
      low = mid+1
  return None

# print(bin_search(list(range(0,10)),5))

#冒泡排序

def bubble_sort(data_li):
  for i in range(len(data_li) - 1):    #每一趟会得到一个有序的数，n个数的数组一共需要走n-1趟
    for j in range(len(data_li) - i -1 ): #第m趟需要比较n-m次,i=0时表示第一趟，所以需要判断n-i-1趟
      if data_li[j] > data_li[j+1]:
        data_li[j],data_li[j+1] = data_li[j+1],data_li[j]   #如果前面的比后面的大，则交换
  return data_li

# print(bubble_sort([5,4,2,3,0]))


# 选择排序
def select_sort(data_li):
  """
  方法:数组分为有序区和无序区，每一堂找到一个最小的元素放入有序区，在每一趟过程中，用另外一个变量记住
      最小的位置的下标，第一趟假设下标为0的数最小，每一趟在比较的过程中会更新最小的那个位置。第i趟确定
      下标为i的个位置的数
  :param data_li:
  :return:
  """
  for i in range(len(data_li)-1):   # 需要走n个数的数组只需要走n-1趟
    min_position = i   #没走一趟首先假设第一个数在无序区最小
    for j in range(i+1, len(data_li)):  #第i趟已经有i-1个数的有序区了，如果range从i开始，表明自己还要跟自己比一次，没有必要
      if data_li[j] < data_li[min_position]:  #如果找到一个数比记录的最小数还要小，更新最小数的位置
        min_position = j
    data_li[min_position], data_li[i] = data_li[i], data_li[min_position]  #遍历完了了之后min_position已经是无序区的最小的数的位置了，这时候只需要和
  return data_li

# a = list(range(100))
# random.shuffle(a)
# print(a)
#
# print(select_sort(a))


#插入排序

def insert_sort0(li):
  for i in range(1, len(li)):     #相当于是抓牌
    tmp = li[i]
    for j in range(0,i):   #表示有序区
      if tmp < li[j]:    #如果发现一个数要比新抓取的要大，说明可以确定新的数的位置了，即为j
        for k in range(i-1, j-1, -1):  #从后往前移
          li[k+1] = li[k]
        li[j] = tmp
        break     #因为前面为有序区，只要又一个数比新抓的数要大，后面的数肯定都要比新数大，所以只需要判断一次即可

def insert_sort1(li):
  for i in range(1, len(li)): #从第第二个数开始，单独把每个数都拿出来，到前面的有序区去比较，相当于是抓牌，手里有一张牌了，从第二种往下面抓
    tmp = li[i]    #先把抓到的牌保存起来
    k = i    #记录空位的下标
    for j in range(i-1, -1, -1):   #range(i-1, -1, -1)表示有序区
      if tmp <= li[j]:
        li[j+1] = li[j]
        k = j
      else:
        k = j+1
        break
    li[k] = tmp
  # return li

def insert_sort2(li):
  for i in range(1,len(li)):   #抓牌，从第二张开始
    tmp = li[i]     #腾出空位
    j = i - 1       #j 的活动区域为有序区
    while j >= 0 and tmp<li[j]:  #当j还在有序区，并且新拿到牌要比有序区的牌要小的时候，比较一次就移动一次
      li[j+1] = li[j]
      j -=1
    li[j+1] = tmp


# a = list(range(100))
# # a = [4,1,2,3,2.2,4.4,2000]
# random.shuffle(a)
# print(a)
# insert_sort2(a)
# print(a)

#快排

#快排归为函数
def partition(li, low, high):
  """
  快排归为函数
  :param li:
  :param low: 左下标
  :param high: 右下标
  :return: 返回某个元素归为后的下标
  """
  tmp = li[low]    #归位的元素为列表的第一个
  while low < high:    #每一轮结束，将会从左边和右边分别调整一个比tmp大的数到右边和一个比tmp小的数到左边
    while low < high and tmp <= li[high]:  #一定要再加上low<high这一个条件，因为在循环里面一直在high--，最后high的值可能会比low的值还小
      high -=1
    li[low] = li[high]
    while low < high and tmp > li[low]:
      low +=1
    li[high] = li[low]
  li[low] = tmp   #循环结束时，low=high,并且这个位置就是tmp在列表中应该在的位置
  return low

def quick_sort(li,low,high):
  """
  首先找到一个元素让他归位，所谓归为即就是让它左边的元素都要比它小，右边的元素都要比他大，
  这样，列表就被分为了两半，再把这两半分别看成两个小列表，应用同样的方法，最后会变成0个或者一个元素的列表
  而这二者都可以看成是有序的。
  :param li:  列表
  :param low:  左下标
  :param high: 右下标
  :return:
  """
  if low < high:  #当左下标小于右下标的时候执行
    mid = partition(li,low,high)
    quick_sort(li, low, mid - 1)   #对左边的小列表使用递归
    quick_sort(li, mid+1, high)   #对右边的小列表使用递归

# a = list(range(10))
# # a = [4,1,2,3]
# random.shuffle(a)
# # print(a)
# quick_sort(a,0,len(a)-1)
# print(a)


# 树的概念
# 数的度，深度，节点
# 二叉树，度为2的树
# 满二叉树，当存在孩子节点时，左右两个孩子节点都存在的二叉树叫满二叉树，
# 完全二叉树，从满二叉树的后面去掉孩子节点，只能从后面往前去
# 堆，有大根堆和小根堆，是一种特殊的完全二叉树，大根堆的父节点值均比孩子节点要大，小根堆相反，根值均比孩子节点的值要小

# 堆的特性，如果左右孩子节点的树都是一个堆，但自身不是堆时，可以通过一次向下的调整(大的值往根上升，)，变成一个堆

#堆排序过程：
# 1. 建立堆，从最后一个孩子点和他的父节点开始调整，保证父节点均比孩子节点要大，依次从后往前，从小往上调整，最终将得到一个堆
# 2. 得到堆顶元素，为最大元素
# 3. 去掉堆顶，将堆最后一个元素放到堆顶，此时可以通过一次调整让堆重新有序
# 4. 堆顶元素为第二大元素
# 5. 重复步骤3，直到堆变空


def shift(li, low, high):
  """
  调整函数，非常关键，建堆和排序的时候都要用到，用来将一个左右孩子均为一个堆，但加上父节点之后就不为堆的二叉树变成一个堆。
  过程为：首先判断是否有左孩子，再判断是否有右孩子，找到左右孩子中最大的一个并和父亲比较，如果父还值小，则大的孩子替换掉父亲
        再向下走，将大的孩子变成父亲，依次类推，最后再讲刚开始保留的父亲的值复制给最后的那个“父亲”
  :param li:
  :param low:  左下标
  :param high: 右下标
  :return:
  """
  i = low  #根节点
  j = 2 * i + 1  #左孩子节点
  tmp = li[i]
  while j <= high:    #左孩子节点还在树的范围之内
    if j < high and li[j] < li[j+1]:    # j<high 说明还有右孩子节点，判断左孩子节点是否比右孩子节点要大，如果比右孩子小，这将j变为右孩子节点
      j += 1    #现在的j为大的右孩子节点
    if tmp < li[j]:  #父节点小于最大的孩子节点，如果为真语句的执行结果就是将孩子节点上位，如果发生了调整，需要继续向下判断
      li[i] = li[j]  #大的孩子节点替换掉父节点
      i = j
      j = 2 * i + 1
    else:   #如果不发生调整，说明根节点要比左右孩子几点都要大，而孩子节点已经是堆了，所以调整就已经结束了
      break
  li[i] = tmp


def heap_sort(li):
  """
  排序过程
  :param li:
  :return:
  """
  n = len(li)
  # 开始建堆，从后往前看，首先找到最后一个孩子(n-1)和他的父亲(n//2-1)的下标,不管列表是奇数还是偶数个，最后一个孩子的父亲总是(n//2-1)
  for i in range(n // 2 -1, -1, -1):    #从最后一个父亲节点开始往前推，能保证除了根节点外左右孩子节点均为堆
    shift(li, i, n - 1)
  # 堆建完了，挨个出数
  for i in range(n - 1, -1, -1):     #从最后一个数开始和根节点调换，这样又变成了根节点最小，但左右孩子树均为堆的情况
    li[0], li[i] = li[i], li[0]    #互换
    shift(li, 0, i-1)  #这个时候列表的最后一个数已经被替换成最大的那个根节点了，也就是列表里面的最大数，新的调整可以剔除最后一个数，


a = list(range(1000000))
# a = [4,1,2,3]
random.shuffle(a)
# print(a)
heap_sort(a)
print(a)
