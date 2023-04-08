from collections import deque

m,n,h = map(int,input().split())
array = [[list(map(int,input().split()))for _ in range(n)]for _ in range(h)]
dx = [-1,0,1,0,0,0]
dy = [0,-1,0,1,0,0]
dz = [0,0,0,0,-1,1]
queue = deque()
visited = [[[-1 for _ in range(m)]for _ in range(n)] for _ in range(h)]

for i in range(h) :
    for j in range(n) :
        for k in range(m) :
            if array[i][j][k] == 1 :
                queue.append((i,j,k))
                visited[i][j][k] = 0
def bfs() :
    while queue :
        x,y,z = queue.popleft()
        for i in range(len(dx)) :
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if -1<nx<h and -1<ny<n and -1<nz<m:
                if array[nx][ny][nz] == 0 :
                    if visited[nx][ny][nz] == -1 :
                        visited[nx][ny][nz] = visited[x][y][z] + 1
                        queue.append((nx,ny,nz))
                        array[nx][ny][nz] = visited[nx][ny][nz]

bfs()
check = True
value = -1
for i in range(h) :
    for j in range(n) :
        for k in range(m) :
            if array[i][j][k] == 0 :
                check = False
            value=max(value,visited[i][j][k])

if check == False :
    print(-1)
else :
    print(value)