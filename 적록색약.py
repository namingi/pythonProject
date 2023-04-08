from collections import deque
n = int(input())
array = []
for i in range(n) :
    array.append(list(map(str,input())))
dx = [-1,0,1,0]
dy = [0,-1,0,1]
visited = [[0 for _ in range(n)]for _ in range(n)]
result = 0
def bfs(x,y) :
    queue = deque()
    queue.append((x,y))
    color = array[x][y]
    while queue :
        x,y= queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if -1<nx<n and -1<ny<n :
                if visited[nx][ny] == 0 :
                    if array[nx][ny] == color :
                        queue.append((nx,ny))
                        visited[nx][ny] = 1
def bfs_2(x,y) :
    queue = deque()
    queue.append((x,y))
    color = array[x][y]
    while queue :
        x,y= queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if -1<nx<n and -1<ny<n :
                if visited_2[nx][ny] == 0 :
                    if array[nx][ny] == color :
                        visited_2[nx][ny] = 1
                        queue.append((nx,ny))
result_2 = 0
visited_2 = [[0 for _ in range(n)]for _ in range(n)]
for i in range(n) :
    for j in range(n) :
        if visited[i][j] == 0 :
            bfs(i,j)
            result +=1
print(result,end=" ")
for i in range(n) :
    for j in range(n) :
        if array[i][j] == "R":
            array[i][j] ="G"
for i in range(n) :
    for j in range(n) :
        if visited_2[i][j] == 0 :
            bfs_2(i,j)
            result_2 +=1
print(result_2)