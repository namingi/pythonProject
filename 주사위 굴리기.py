n,m,x,y,k = map(int,input().split())
array = []
for _ in range(n) :
    array.append(list(map(int,input().split())))
order = list(map(int,input().split()))
dx = [0,0,-1,1]
dy = [1,-1,0,0]
rock = [0,0,0,0,0,0]
def turn(dir,array) :
    a,b,c,d,e,f = array[0],array[1],array[2],array[3],array[4],array[5]
    if dir == 1 :
        array[0], array[1], array[2], array[3], array[4], array[5] = d,b,a,f,e,c
    elif dir == 2 :
        array[0],array[1],array[2],array[3],array[4],array[5] = c,b,f,a,e,d
    elif dir == 3 :
        array[0], array[1], array[2], array[3], array[4], array[5] = e,a,c,d,f,b
    else :
        array[0], array[1], array[2], array[3], array[4], array[5] = b, f, c, d, a, e
    return array

nx, ny = x, y
for i in order:
    nx += dx[i-1]
    ny += dy[i-1]
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        nx -= dx[i-1]
        ny -= dy[i-1]
        continue
    rock = turn(i,rock)
    if array[nx][ny] == 0:
        array[nx][ny] = rock[-1]
    else:
        rock[-1] = array[nx][ny]
        array[nx][ny] = 0
    print(rock[0])