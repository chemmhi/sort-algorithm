# Author: Chenchen

import random

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


