from collections import deque
import math
N,L,R = map(int,input().split())
array = []
for _ in range(N) :
    array.append(list(map(int,input().split())))
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(x,y) :
    queue = deque()
    queue.append((x,y))
    visited[x][y] = 1
    score = array[x][y]
    union = [(x,y)]
    while queue :
        x,y = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if -1<nx<N and -1<ny<N :
                if not visited[nx][ny] :
                    if L<=abs(array[nx][ny]-array[x][y])<=R :
                        visited[nx][ny] = 1
                        queue.append((nx,ny))
                        union.append((nx,ny))
                        score += array[nx][ny]
    for x,y in union :
        array[x][y] = math.floor(score/len(union))
    return len(union)
cnt = 0
while True :
    visited = [[0 for _ in range(N)]for _ in range(N)]
    flag = False
    for i in range(N) :
        for j in range(N) :
            if not visited[i][j] :
                if bfs(i,j) >1 :
                    flag = True

    if not flag :
        break
    cnt += 1
print(cnt)
