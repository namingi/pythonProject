import copy
from collections import deque
r,c,t = map(int,input().split())
array = []
dx = [-1,0,1,0]
dy = [0,1,0,-1]
for _ in range(r) :
    array.append(list(map(int,input().split())))

def dust_move() :
    while queue :
        x,y,dust = queue.popleft()
        total = dust
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if -1<nx<r and -1<ny<c :
                if array[nx][ny] != -1 :
                    visited[nx][ny] += int(dust/5)
                    total -= int(dust/5)
        visited[x][y] += total

def move():
    x,y = clean.pop(0)

    temp = visited[x][c-1]
    for i in range(c-1,1,-1) :
        visited[x][i] = visited[x][i-1]
    visited[x][1] = 0

    temp_2 = visited[0][c-1]
    for i in range(x-1) :
        visited[i][c-1] = visited[i+1][c-1]
    visited[x-1][c-1] = temp

    temp_3 = visited[0][0]
    for i in range(c-2) :
        visited[0][i] = visited[0][i+1]
    visited[0][c-2] = temp_2

    for i in range(x-1,1,-1) :
        visited[i][0] =  visited[i-1][0]
    visited[1][0] = temp_3

    x,y = clean.pop(0)

    temp = visited[x][c-1]
    for i in range(c-1,1,-1) :
        visited[x][i] = visited[x][i-1]
    visited[x][1] = 0

    temp_2 = visited[r-1][c-1]
    for i in range(r-1,x+1,-1) :
        visited[i][c-1] = visited[i-1][c-1]
    visited[x+1][c-1] = temp

    temp_3 = visited[r-1][0]
    for i in range(c-2) :
        visited[r-1][i] = visited[r-1][i+1]
    visited[r-1][c-2] = temp_2

    for i in range(x+1,r-1) :
        visited[i][0] = visited[i+1][0]
    visited[r-2][0] = temp_3
time = 0
while True :
    queue = deque()
    visited = [[0 for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if array[i][j] != -1 and array[i][j] != 0:
                queue.append((i, j, array[i][j]))
            if array[i][j] == -1:
                visited[i][j] = -1
    clean = []
    for i in range(r):
        for j in range(c):
            if visited[i][j] == -1:
                clean.append((i, j))
    dust_move()
    move()
    time += 1
    if time ==  t :
        break
    array = copy.deepcopy(visited)
result = 0
for i in range(len(visited)) :
    for j in range(len(visited[i])) :
        if visited[i][j] > 0 :
            result += visited[i][j]
print(result)
