from collections import deque
import sys
n,m = map(int,sys.stdin.readline().split())
array= []
for i in range(n) :
    array.append(list(map(int,sys.stdin.readline().split())))
virus = []
select = [0 for _ in range(10)]
for i in range(n) :
    for j in range(n) :
        if array[i][j] == 2 :
            virus.append((i,j))

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def bfs() :
    flag = True
    queue= deque()
    ans = -1
    distance = [[-1 for _ in range(n)] for _ in range(n)]
    for i in range(len(virus)):
        if select[i]:
            queue.append((virus[i][0], virus[i][1]))
            distance[virus[i][0]][virus[i][1]] = 0
    for i in range(n) :
        for j in range(n) :
            if array[i][j] == 1 :
                distance[i][j] = "-"


    while queue :
        x,y = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if -1<nx<n and -1<ny<n :
                if distance[nx][ny] != "-" :
                    if distance[nx][ny] == -1 :
                        distance[nx][ny] = distance[x][y] + 1
                        queue.append((nx,ny))
    for i in range(n) :
        for j in range(n) :
            if distance[i][j] !="-" :
                ans= max(ans,distance[i][j])
            if distance[i][j] == -1 :
                flag = False
    if flag == True :
        return ans
    else :
        return -1
answer = 9999
def recursive(cnt,idx) :
    global answer
    if cnt == m :
        value = bfs()
        if value != -1 :
            answer = min(answer,value)
        return
    for i in range(idx,len(virus)) :
        if not select[i] :
            select[i]= 1
            recursive(cnt+1,i+1)
            select[i] = 0
recursive(0,0)
if answer == 9999 :
    print(-1)
else :
    print(answer)
