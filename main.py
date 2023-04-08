n = int(input())
from collections import deque
shark_size = 2
array = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n) :
    array[i] = list(map(int, input().split()))

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(st_x,st_y) :
    queue = deque()
    queue.append((st_x,st_y))
    array[st_x][st_y] = 0
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    visited[st_x][st_y] = 0
    while queue :
        x,y = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if -1<nx<n and -1<ny<n :
                if visited[nx][ny] == -1 :
                    if array[nx][ny] <=shark_size :
                        visited[nx][ny] = visited[x][y] + 1
                        queue.append((nx,ny))
    return visited

target = []
def find(dist) :
    flag = True
    min_dist = 9999
    global shark_size
    for i in range(n) :
        for j in range(n) :
            if 0<array[i][j] < shark_size :
                if dist[i][j] != -1 :
                    if dist[i][j] < min_dist :
                        x,y = i,j
                        min_dist = dist[i][j]
    if min_dist == 9999 :
        return 0
    else :
        return x,y,min_dist


time = 0
cnt = 0
tmp = []

while True :
    for i in range(n) :
        for j in range(n) :
            if array[i][j] == 9 :
                x,y = i,j
    value =  find(bfs(x,y))
    if value != 0 :
        time += value[2]
        array[value[0]][value[1]] = 9
        cnt += 1
        if cnt == shark_size :
            shark_size+=1
            cnt = 0
    else :
        break
print(time)