from collections import deque
dx = [-1,0,1,0]
dy = [0,1,0,-1]
array = []
cnt = 0
n = 12
m= 6
for _ in range(12) :
    array.append(list(map(str,input())))
def bfs(i,j) :
    global cnt
    size = 1
    tangle=array[i][j]
    queue = deque()
    queue.append((i,j))
    visited[i][j] = 1
    temp = []
    moved = False
    temp.append((i,j))
    while queue :
        x,y = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if -1<nx<n and -1<ny<m :
                if not visited[nx][ny] :
                    if array[nx][ny] == tangle :
                        visited[nx][ny] = 1
                        queue.append((nx,ny))
                        temp.append((nx,ny))
                        size += 1
    if size >= 4  :
        while len(temp) :
            x,y = temp.pop(0)
            array[x][y] = "."
        moved = True
    return moved

def move() :
    for i in range(n - 1, -1, -1):
        for j in range(m):
            if array[i][j] == '.':
                for s in range(i - 1, -1, -1):
                    if array[s][j] != '.':
                        array[i][j] = array[s][j]
                        array[s][j] = '.'
                        break
answer= 0
while True :
    flag = False
    visited = [[0 for _ in range(len(array[0]))] for _ in range(len(array))]
    for i in range(len(array)) :
        for j in range(len(array[0])) :
            if array[i][j] != "." and visited[i][j] == 0 :
                flag = bfs(i,j)
    move()
    if flag == True :
        answer += 1
        break
    else :
        break
print(answer)