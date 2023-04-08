from collections import deque
import sys
input = lambda : sys.stdin.readline()
n,m = map(int,input().split())

array = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n) :
    array[i] = list(map(int,input().split()))

dx = [-1,0,1,0]
dy = [0,1,0,-1]
def bfs(x,y) :
    queue = deque()
    queue.append((x,y))
    visited = [[0 for _ in range(m)] for _ in range(n)]
    visited[x][y] = 1
    while queue :
        x,y = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if -1<nx<n and -1<ny<m :
                if not visited[nx][ny] and array[nx][ny]>0 :
                    visited[nx][ny] = 1
                    queue.append((nx,ny))
                if array[nx][ny] == 0 and visited[nx][ny] == 0 :
                    if array[x][y] > 0 :
                        array[x][y] -= 1

def bfs_2(x,y) :
    queue = deque()
    queue.append((x,y))
    while queue :
        x,y = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if -1<nx<n and -1<ny<m :
                if array[nx][ny] != 0 :
                    if not visited_2[nx][ny] :
                        visited_2[nx][ny] = 1
                        queue.append((nx,ny))

time = 0
while True :
    check = True
    result = 0
    visited_2 = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(len(array)) :
        for j in range(len(array[i])) :
            if array[i][j] != 0 :
                bfs(i,j)
                time += 1
                check = False
                break
        if check == False :
            break
    for i in range(n) :
        for j in range(m) :
            if array[i][j] != 0 and not visited_2[i][j] :
                bfs_2(i,j)
                result +=1
    if result > 1 :
        break
print(time)
