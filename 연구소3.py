import copy
from collections import deque
n,m = map(int,input().split())
array = []
virus = []
for _ in range(n) :
    array.append(list(map(int,input().split())))
secure_cnt = 0
for i in range(n) :
    for j in range(n) :
        if array[i][j] == 2 :
            virus.append((i,j))
        if array[i][j] ==0 :
            secure_cnt += 1

select = [0 for _ in range(10)]
dx = [-1,0,1,0]
dy = [0,-1,0,1]
ans = 9999
def dfs(tmp,idx) :
    global answer
    if tmp == m :
        bfs()
        return
    for i in range(idx,len(virus)) :
        if not select[i] :
            select[i] = 1
            dfs(tmp+1,i+1)
            select[i] = 0
def bfs() :
    queue = deque()
    global secure_cnt
    global ans
    time = 0
    zero_cnt = 0
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    check = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(10):
        if select[i]:
            queue.append((virus[i][0], virus[i][1]))
            visited[virus[i][0]][virus[i][1]] =0
            check[virus[i][0]][virus[i][1]] = 1

    while queue :
        x,y = queue.popleft()
        for i in range(4) :
            nx = x +dx[i]
            ny = y + dy[i]
            if -1<nx<n and -1<ny<n :
                if visited[nx][ny] == -1 and array[nx][ny] != 1   :
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx,ny))
                    if array[nx][ny] == 0 :
                        zero_cnt += 1
                        time = visited[nx][ny]
    if zero_cnt == secure_cnt :
        ans = min(ans,time)


dfs(0,0)
if ans == 9999 :
    print(-1)
else :
    print(ans)
