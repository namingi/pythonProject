from collections import deque

r,c = map(int,input().split())

array = []
for _ in range(r) :
    array.append(list(map(str, input())))
dx = [-1,0,1,0]
dy = [0,-1,0,1]
visited_fire = [[- 1 for _ in range(c)] for _ in range(r)]
visited = [[-1 for _ in range(c)] for _ in range(r)]

def bfs_fire(x,y) :
    queue = deque()
    queue.append((x,y))
    visited_fire[x][y] = 0
    while queue :
        x,y = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if -1<nx<r and -1<ny<c :
                if array[nx][ny] != "#" :
                    if array[nx][ny] != "J" :
                         if visited_fire[nx][ny] == -1 :
                            visited_fire[nx][ny] = visited_fire[x][y] + 1
                            queue.append((nx,ny))
def bfs(x,y) :
    person = deque()
    person.append((x,y))
    visited[x][y] = 0
    string = "IMPOSSIBLE"
    while person :
        x,y = person.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=r or ny>=c :
                value = visited[x][y]+1
                return value
            if visited[nx][ny] != -1 or array[nx][ny] =="#" or (visited_fire[nx][ny] !=-1 and visited_fire[nx][ny] <=visited[x][y]+1) :
                continue
            if array[nx][ny] != "F" :
                visited[nx][ny] = visited[x][y] + 1
                person.append((nx,ny))
    return string
for i in range(r) :
    for j in range(c) :
        if array[i][j] == "F" :
            f_x,f_y = i,j
        if array[i][j] == "J" :
            j_x, j_y = i,j
bfs_fire(f_x,f_y)
print(bfs(j_x,j_y))