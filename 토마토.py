from collections import deque

m,n = map(int,input().split())
array = [[0 for _ in range(m)] for _ in range(n)]
visited = [[-1 for _ in range(m)] for _ in range(n)]
for i in range(n) :
    array[i] = list(map(int,input().split()))

dx = [-1,0,1,0]
dy = [0,-1,0,1]
queue = deque()
def bfs() :
    while queue :
        x,y = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if -1<nx<n and -1<ny<m :
                if visited[nx][ny] == -1 :
                    if array[nx][ny] != -1 :
                        visited[nx][ny] = visited[x][y] + 1
                        queue.append((nx,ny))
                        array[nx][ny] = visited[nx][ny]
for i in range(n) :
    for j in range(m) :
        if array[i][j] == 1 :
            queue.append((i,j))
            visited[i][j] = 0
bfs()
check = True
value = -1
for i in range(n) :
    for j in range(m) :
        if array[i][j] == 0 :
            check = False
        value = max(value,visited[i][j])
if check == False :
    print(-1)
else :
    print(value)

