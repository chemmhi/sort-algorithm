# Author: Chenchen

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
