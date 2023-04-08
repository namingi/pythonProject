from collections import deque

n,m,g,r = map(int,input().split())
array = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n) :
    array[i] = list(map(int,input().split()))

visited = [[0 for _ in range(m)] for _ in range(n)]
result = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
value = 0

def recur(n) :
    global value
    if n == (r+g) :
        queue_r = deque()
        queue_g = deque()
        visited = [[[0,0] for _ in range(m)] for _ in range(n)]
        for i in range(g,g+r):
            x, y = result[i]
            queue_r.append((x, y))
            visited[x][y][1] = 4
        for j in range(g):
            x, y = result[j]
            queue_g.append((x, y))
            visited[x][y][1] = 3
        size = 0
        while queue_r:
            x, y = queue_r.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if -1 < nx < n and -1 < ny < m:
                    if array[nx][ny] == 1 or array[nx][ny] == 2:
                        if not visited[nx][ny]:
                            visited[nx][ny] = visited_R[x][y] + 1
                            queue_r.append((nx, ny))
        while queue_g:
            x, y = queue_g.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if -1 < nx < n and -1 < ny < m:
                    if array[nx][ny] == 1 or array[nx][ny] == 2:
                        if not visited_G[nx][ny]:
                            visited_G[nx][ny] = visited_G[x][y] + 1
                            queue_g.append((nx, ny))
        for i in range(n):
            for j in range(m):
                if array[i][j] == 1:
                    if visited_R[i][j] != 1 or visited_G[i][j] != 1 :
                        if visited[i][j] == visited_G[i][j]:
                            size += 1
        value = max(size,value)

    for i in range(len(array)) :
        for j in range(len(array[i])) :
            if not visited[i][j] :
                if array[i][j] == 2 :
                    visited[i][j] = 1
                    result.append([i,j])
                    recur(n+1)
                    result.pop()
                    visited[i][j] = 0
recur(0)
print(value)