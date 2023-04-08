from collections import deque

dx = [-1,0,1,0]
dy = [0,-1,0,1]
queue = deque()
def bfs(x,y) :
    queue.append((x,y))
    array[x][y] = 0
    while queue :
        x,y = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if -1<nx<m and -1<ny<n :
                if array[nx][ny] == 1:
                    array[nx][ny] = 0
                    queue.append((nx,ny))
T = int(input())
for i in range(1,T+1) :
    result = 0
    m,n,k = map(int,input().split())
    array = [[0 for _ in range(n)]for _ in range(m)]
    for i in range(k) :
        x,y = map(int,input().split())
        array[x][y] = 1
    for i in range(m) :
        for j in range(n) :
            if array[i][j] == 1 :
                bfs(i,j)
                result +=1
    print(result)


