from collections import deque
n,m,k = map(int,input().split())

array = []
for _ in range(n) :
    array.append(list(map(int,input().split())))
axis = []
start_x,start_y = map(int,input().split())
for _ in range(m) :
    axis.append(list(map(int,input().split())))
axis.sort(key = lambda x : (x[0],x[1]))

dx = [-1,0,1,0]
dy = [0,1,0,-1]
def bfs(x,y) :
    queue = deque()
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    queue.append((x,y))
    visited[x][y] = 0
    while queue :
        x,y = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if -1<nx<n and -1<ny<n and array[nx][ny] != 1 :
                if visited[nx][ny] == -1 :
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx,ny))

    return visited
length = len(axis)
while axis :
    min_dist = 9999
    dist = bfs(start_x-1,start_y-1)
    s_idx = 0
    for idx in range(len(axis)) :
        value = dist[axis[idx][0]-1][axis[idx][1]-1]
        if value == -1 :
            continue
        if value <min_dist :
            min_dist = value
            s_x = axis[idx][0]
            s_y = axis[idx][1]
            s_idx = idx
        elif value == min_dist :
            if s_x>axis[idx][0] :
                s_x = axis[idx][0]
                s_y = axis[idx][1]
                s_idx = idx
            elif s_x == axis[idx][0] :
                if s_y>axis[idx][1] :
                    s_y = axis[idx][1]
                    s_idx = idx
    if min_dist ==  9999 :
        break
    start_x,start_y,target_x,target_y = axis.pop(s_idx)
    k -= min_dist
    if k<=0 :
        break
    dist = bfs(start_x-1,start_y-1)
    value = dist[target_x-1][target_y-1]
    if value == -1 :
        break
    k -= value
    if k< 0 :
        break

    start_x,start_y = target_x,target_y
    length -= 1
    k += value*2
if length > 0 :
    print(-1)
else :
    print(k)
