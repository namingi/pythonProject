from collections import deque
dx = [-1,0,1,0]
dy = [0,-1,0,1]
n = int(input())
array = []
for i in range(n) :
    array.append(list(map(int,input())))
target = []
def bfs(x,y) :
    queue = deque()
    queue.append((x,y))
    array[x][y] = 0
    size = 1
    while queue :
        x,y = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if -1<nx<n and -1<ny<n :
                if array[nx][ny] == 1 :
                    queue.append((nx,ny))
                    array[nx][ny] = 0
                    size += 1
    return size

for i in range(n) :
    for j in range(n) :
        if array[i][j] == 1 :
            value = bfs(i,j)
            target.append(value)
print(len(target))
target.sort()
for i in range(len(target)) :
    print(target[i])