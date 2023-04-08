n = int(input())
from collections import deque

dx = [-1,0,1,0]
dy = [0,-1,0,1]
def bfs(x,y) :
    queue = deque()
    queue.append((x,y))
    visited[x][y] = 1
    while queue :
        x,y = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if -1<nx<n and -1<ny<n :
                if array[nx][ny] > h and not visited[nx][ny] :
                    visited[nx][ny] = 1
                    queue.append((nx,ny))

array = []
for _ in range(n) :
    array.append(list(map(int,input().split())))
num = 0
for i in range(len(array)) :
    for j in range(len(array[i])) :
        num = max(num,array[i][j])
h = 1
result = 0
while h <= num :
    value = 0
    visited = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(len(array)) :
        for j in range(len(array[i])) :
            if array[i][j] > h and not visited[i][j]:
                visited[i][j] = 1
                bfs(i,j)
                value +=1
    result = max(value,result)
    h+=1
print(result)


