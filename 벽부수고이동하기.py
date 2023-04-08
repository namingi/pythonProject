from collections import deque
n,m = map(int,input().split())
array = []
for i in range(n) :
    array.append(list(map(int,input())))
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs() :
    queue = deque()
    queue.append((0,0,0))
    visited = [[[0 for _ in range(2)] for _ in range(m)] for _ in range(n)]
    visited[0][0][0] = 1
    while queue :
        x,y,wall = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if -1<nx<n and -1<ny<m :
                if array[nx][ny] == 0 :
                    if visited[nx][ny][wall] == 0 :
                        visited[nx][ny][wall] = visited[x][y][wall] + 1
                        queue.append((nx,ny,wall))
                if array[nx][ny] == 1 and wall == 0 :
                    if visited[nx][ny][wall] == 0 :
                        visited[nx][ny][1] = visited[x][y][wall] + 1
                        queue.append((nx,ny,1))


    return visited[n-1][m-1][wall]

if bfs() == 0:
    print(-1)
else :
    print(bfs())
