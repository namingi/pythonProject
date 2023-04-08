from collections import deque

M,N,K = map(int,input().split())
array = [[0 for _ in range(N)] for _ in range(M)]
for _ in range(K) :
    s_x,s_y,d_x,d_y = map(int,input().split())
    for i in range(s_y,d_y) :
        for j in range(s_x,d_x) :
            if array[i][j] == 0 :
                array[i][j] +=1
def rotate(array) :
    matrix = [[0 for _ in range(N)]for _ in range(M)]
    for i in range(len(array)):
        for j in range(len(array[i])) :
            matrix[i][j] = array[M-i-1][j]
    return matrix
array = rotate(array)
visited =[[0 for _ in range(N)] for _ in range(M)]
dx = [-1,0,1,0]
dy = [0,-1,0,1]
def bfs(y,x) :
    queue = deque()
    queue.append((y,x))
    array[y][x] = 0
    size = 0
    while queue :
        y,x = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if -1<nx<N and -1<ny<M :
                if array[ny][nx] == 0 :
                    queue.append((ny,nx))
                    array[ny][nx] = 1
                    size += 1
    if size == 0  :
        return 1
    else :
        return size
target = []
for i in range(M) :
    for j in range(N) :
        if array[i][j] == 0 :
           value =  bfs(i,j)
           target.append(value)
target.sort()
print(len(target))
for i in range(len(target)) :
    print(target[i],end=" ")
