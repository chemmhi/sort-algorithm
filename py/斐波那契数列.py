# Author: Chenchen
#形如1, 1, 2, 3, 5, 8, 13, 21, 34, 55的数列，
# 后一位是前面两位相加（斐波那契数列），写出函数要求找到第 N 位是多少，
# 如：fib(3) => 3 ， fib(5) => 8, 要求时间复杂度为O(n)。
import sys
sys.setrecursionlimit(100000)


def fib(num):
    #如果num=1,return1
    #如果num=2，return2
    #如果num>2,
    if num == 0 or num == 1:
        res = 1
        return res
    return fib(num-1) + fib(num-2)

from collections import deque

def fib2(num):
    if num < 0:
        return '输入有误'
    else:
        queue = deque([1, 1, ], maxlen=3)
        i = 1   #下标
        while i < num and i >= 1:
            tmp2 = queue.popleft()
            queue.append(queue[0] + tmp2)
            i +=1
        return queue[-1]
print(fib2(1000))