from sys import stdin
n,m,k = map(int,stdin.readline().split())
from collections import deque
array = []

for i in range(n) :
    array.append(list(map(int,stdin.readline().strip())))

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def bfs() :
    queue = deque()
    queue.append((0,0,0))
    visited = [[[0] * (k + 1) for _ in range(m)] for _ in range(n)]
    visited[0][0][0] = 1
    while queue :
        x,y,wall = queue.popleft()
        if x == n-1 and y == m -1 :
            return visited[x][y][wall]
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if -1<nx<n and -1<ny<m :
                if visited[nx][ny][wall] == 0  :
                    if array[nx][ny] == 0 :
                        visited[nx][ny][wall] = visited[x][y][wall] + 1
                        queue.append((nx,ny,wall))
                    else :
                        if wall < k :
                            visited[nx][ny][wall+1] = visited[x][y][wall]+1
                            queue.append((nx,ny,wall+1))
    return -1

value = bfs()
print(value)