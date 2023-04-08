from collections import deque
import copy
n,m = map(int,input().split())
array = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n) :
    array[i] = list(map(int,input().split()))
dx = [-1,0,1,0]
dy = [0,1,0,-1]
def bfs(queue,visited,array) :
    tmp_graph = copy.deepcopy(array)
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if not visited[nx][ny] :
                if tmp_graph[nx][ny] == 0:
                    tmp_graph[nx][ny] = 2
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
    return tmp_graph

answer = 0
def recursive(tmp) :
    global answer
    if tmp == 3 :
        size = 0
        queue = deque()
        visited = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n) :
            for j in range(m) :
                if array[i][j] == 2 :
                    queue.append((i,j))
                    visited[i][j] = 1
        tmp = bfs(queue,visited,array)
        for i in range(n):
            for j in range(m) :
                if tmp[i][j] == 0 :
                    size += 1
        answer = max(size,answer)
        return
    for i in range(n) :
        for j in range(m) :
            if array[i][j] == 0 :
                array[i][j] = 1
                recursive(tmp+1)
                array[i][j] = 0
recursive(0)
print(answer)