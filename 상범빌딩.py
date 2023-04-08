from collections import deque

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

def bfs() :
    while queue :
        x,y,z = queue.popleft()
        if z == dest_z and y == dest_y and x == dest_x :
            return visited[z][x][y]+1
        for i in range(6) :
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if -1<nz<L and -1<nx<R and -1<ny<C :
                if array[nz][nx][ny] !="#" :
                    if visited[nz][nx][ny] == -1 :
                        visited[nz][nx][ny] = visited[z][x][y] + 1
                        queue.append((nx,ny,nz))
while True :
    L,R,C = map(int,input().split())
    visited = [[[-1 for _ in range(C)] for _ in range(R)] for _ in range(L)]
    if L==0 and R==0 and C==0 :
        break
    array = [[] for _ in range(L)]
    for k in range(L) :
        for i in range(R) :
            array[k].append(list(map(str,input())))
        input()
    queue = deque()
    for k in range(L) :
        for i in range(R) :
            for j in range(C) :
                if array[k][i][j] == "S" :
                    queue.append((i,j,k))
                if array[k][i][j] == "E" :
                    dest_x,dest_y,dest_z = i,j,k
    value = bfs()
    if value == None :
        print("Trapped!")
    else :
        print("Escaped in %d minute(s)."%value)