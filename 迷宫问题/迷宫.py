# Author: Chenchen

maze = [
    [1,1,1,1,1,1,1,1,1,1], #0
    [1,0,0,1,0,0,0,1,0,1], #1
    [1,0,0,1,0,0,0,1,0,1], #2
    [1,0,0,0,0,1,1,0,0,1], #3
    [1,0,1,1,1,0,0,0,0,1], #4
    [1,0,0,0,1,0,2,0,0,1], #5
    [1,0,1,0,0,0,1,0,0,1], #6
    [1,0,1,1,1,0,1,1,0,1], #7
    [1,1,0,0,0,0,0,2,0,1], #8
    [1,1,1,1,1,1,1,1,1,1], #9
]
directions = [
    lambda x, y: (x, y + 1),
    lambda x, y: (x + 1, y),
    lambda x, y: (x, y - 1),
    lambda x, y: (x - 1, y),
]

#深度优先
def getPath(startCoordinate,endCoordinate):
    stack = []
    stack.append(startCoordinate)
    while len(stack) != 0:
        current = stack[-1]
        if current == endCoordinate:  #说明到终点了
            return stack
        else:
            for dir in directions:
                next = dir(*current)   #next = (x,y)
                if maze[next[0]][next[1]] == 0:  #说明没有碰到墙
                    stack.append(next)    #将下一步能走的进栈
                    maze[next[0]][next[1]] = -1
                    break
            else:   #四个方向都走了，说明是死路，回退一步
                maze[current[0]][current[1]] = -1
                stack.pop()
    return ['Imposible']



# 广度优先
from collections import deque

def handlePath(path):
    tmp = []
    tmp.append((path[-1][0], path[-1][1]))
    i = path[-1][2]
    while i >= 0:
        tmp.append((path[i][0],path[i][1]))
        i = path[i][2]
    tmp.reverse()
    return tmp

def getPath2(startCoordinate,endCoordinate):
    queue = deque([])
    path = []
    queue.append((*startCoordinate,-1))  #开始坐标进队
    while len(queue) !=0:  #当队列不为空时循环
        current = queue.popleft()   #出队
        path.append(current)   #将出队的元素保留起来，用来查找路径
        if (current[0],current[1]) == endCoordinate: #说明到达终点
            return handlePath(path)
        else:   #说明不是终点，要找下一步
            for dire in directions:   #将所有能进队的点均进队
                next = dire(current[0],current[1])
                if maze[next[0]][next[1]] == 0:  #当前说明有路可走
                    queue.append((*next,len(path)-1))  #将下一个节点加入到队列之中
                    #将节点加入队中后，要记录下是谁让他进队的
                    maze[next[0]][next[1]] = -1  #标记新加的节点

    return ['Impossible']

res = getPath2((1,1),(8,8))
print(res)
# for i in res:
#     print(i)
