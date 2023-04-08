from collections import deque
n = int(input())
k = int(input())
array = [[0 for _ in range(n+1)] for _ in range(n+1)]
clock = []
for _ in range(k) :
    x,y = map(int,input().split())
    array[x][y] = 1
l = int(input())
for _ in range(l) :
    shift,dir = map(str,input().split())
    clock.append((int(shift),dir))
dx = [0,1,0,-1]
dy = [1,0,-1,0]
dir = [0,1,2,3]
def direction(current,dir) :
    if dir == "D" :
        now = (current+1)%4
    else :
        now = (current-1)%4
    return now
array[1][1] = 2
time = 0
def simul() :
    global time
    queue = deque()
    queue.append((1,1))
    x,y = 1,1
    array[1][1] = 2
    di = 0
    while True :
        nx= x + dx[di]
        ny= y + dy[di]
        if 1<=nx<=n and 1<=ny<=n and array[nx][ny] != 2 :
            if array[nx][ny] == 1 :
                queue.append((nx,ny))
                time += 1
                array[nx][ny] = 2
            elif array[nx][ny] == 0 :
                array[nx][ny] = 2
                queue.append((nx,ny))
                time += 1
                tail_x,tail_y = queue.popleft()
                array[tail_x][tail_y] = 0
        else :
            time += 1
            break
        x,y = nx,ny
        for i in range(len(clock)) :
            if clock[i][0] == time :
                di = direction(di,clock[i][1])

simul()
print(time)