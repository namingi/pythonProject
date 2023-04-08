n,m = map(int,input().split())
from collections import deque
array = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n) :
    array[i] = list(map(int,input()))
dx = [-1,0,1,0]
dy = [0,-1,0,1]


visited = [[-1 for _ in range(m)] for _ in range(n)]

def bfs(x,y) :
    queue = deque()
    queue.append((x,y))
    visited[x][y] = 0
    while queue :
        x,y = queue.popleft()
        for i in range(4) :
            nx = x+ dx[i]
            ny = y + dy[i]
            if -1<nx<n and -1<ny<m :
                if array[nx][ny]==1 :
                    if visited[nx][ny] == -1 :
                        visited[nx][ny] = visited[x][y] + 1
                        queue.append((nx,ny))
    return visited[n-1][m-1] +1

print(bfs(0,0))


