from collections import deque

n = int(input())
array = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n) :
    array[i] = list(map(int,input().split()))

dx = [-1,0,1,0]
dy = [0,1,0,-1]
visited = [[0 for _ in range(n)] for _ in range(n)]

def bfs(x,y) :
    global result
    queue = deque()
    queue.append((x,y))
    visited[x][y] = 1
    array[x][y] = result
    while queue :
        x,y = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if -1<nx<n and -1<ny<n :
                if not visited[nx][ny] :
                    if array[nx][ny] == 1 :
                        visited[nx][ny] = 1
                        queue.append((nx,ny))
                        array[nx][ny] = result
result = 0
for i in range(n) :
    for j in range(n) :
        if array[i][j] == 1 and not visited[i][j] :
            result+= 1
            bfs(i,j)
answer = 9999
def bfs_2(flag) :
    global answer
    queue = deque()
    visited_2 = [[-1 for _ in range(n)] for _ in range(n)]
    for i in range(n) :
        for j in range(n) :
            if array[i][j] == flag :
                queue.append((i,j))
                visited_2[i][j] = 0
    while queue :
        x,y = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if -1<nx<n and -1<ny<n :
                if visited_2[nx][ny] == -1 :
                    if array[nx][ny] == 0 :
                        visited_2[nx][ny] = visited_2[x][y]+1
                        queue.append((nx,ny))
                if array[nx][ny] > 0 and array[nx][ny] != flag:
                    answer = min(answer, visited_2[x][y])

for i in range(1,result+1) :
    bfs_2(i)
print(answer)
