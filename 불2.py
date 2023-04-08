from collections import deque

def bfs() :
    string = "IMPOSSIBLE"
    while queue :
        x,y = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if -1<nx<h and -1<ny<w :
                if visited_fire[nx][ny] == -1 and array[nx][ny] !="#" :
                    visited_fire[nx][ny] = visited_fire[x][y] + 1
                    queue.append((nx,ny))
    while person :
        x,y = person.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx >= h or ny<0 or ny >= w :
                value = visited[x][y] + 1
                return value
            if array[nx][ny] != "#" and visited[nx][ny] == -1 :
                if visited_fire[nx][ny]==-1 or visited_fire[nx][ny] > visited[x][y] + 1 :
                    visited[nx][ny] = visited[x][y] + 1
                    person.append((nx,ny))
    return string
t = int(input())
for _ in range(1,t+1) :
    w, h = map(int, input().split())
    array = []
    queue = deque()
    person = deque()
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    for j in range(h) :
        array.append(list(map(str,input())))
    visited_fire = [[-1 for _ in range(w)]for _ in range(h)]
    visited = [[-1 for _ in range(w)] for _ in range(h)]
    for i in range(h) :
        for j in range(w) :
            if array[i][j] == "*" :
                queue.append((i,j))
                visited_fire[i][j] = 0
            if array[i][j] =="@" :
                person.append((i,j))
                visited[i][j] = 0
    print(bfs())