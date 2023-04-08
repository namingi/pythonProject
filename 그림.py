from collections import deque
n,m = map(int,input().split())

array = [[0 for _ in range(m)] for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n) :
    array[i] = list(map(int, input().split()))

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(x,y) :
    queue = deque()
    queue.append((x,y))
    visited[x][y] = 1
    size = 1
    while queue :
        x,y = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if -1<nx<n and -1<ny<m :
                if array[nx][ny] == 1 :
                    if visited[nx][ny] == 0 :
                        queue.append((nx,ny))
                        visited[nx][ny] = 1
                        array[nx][ny] = 0
                        size += 1
    return size
target = []
for i in range(n) :
    for j in range(m) :
        if array[i][j] == 1 :
            value = bfs(i,j)
            target.append(value)
print(len(target))
if not target:
    print(0)
else:
    print(max(target))