from collections import deque

T = int(input())
dx = [-2,-2,-1,-1,1,1,2,2]
dy = [-1,1,-2,2,-2,2,-1,1]
def bfs(x,y) :
    queue = deque()
    queue.append((x,y))
    while queue :
        x,y = queue.popleft()
        if x == dest_x and y == dest_y :
            return array[x][y]
        for i in range(8) :
            nx = x + dx[i]
            ny = y + dy[i]
            if -1<nx<n and -1<ny<n :
                if array[nx][ny] == 0 :
                    queue.append((nx,ny))
                    array[nx][ny] = array[x][y] + 1

for _ in range(1,T+1) :
    n = int(input())
    array = [[0 for _ in range(n)] for _ in range(n)]
    x,y = map(int,input().split())
    dest_x,dest_y = map(int,input().split())
    print(bfs(x,y))

