from collections import deque

n,m = map(int,input().split())
queue= deque()
queue.append(n)
array = [0]*(100001)
def bfs() :
    while queue :
        n = queue.popleft()
        if n == m :
            break
        if -1<n-1<len(array):
            if array[n-1] == 0:
                array[n-1]= array[n] + 1
                queue.append(n - 1)
        if -1<n+1<len(array) :
            if array[n+1] == 0:
                array[n + 1] = array[n] + 1
                queue.append(n + 1)
        if -1<2*n<len(array) :
            if array[2*n] == 0 :
                array[2*n] = array[n] + 1
                queue.append(2*n)
bfs()
print(array[m])
