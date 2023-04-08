n,m = map(int,input().split())

r,c,dir = map(int,input().split())
array = []
visited = [[0 for _ in range(m)] for _ in range(n)]
for _ in range(n) :
    array.append(list(map(int,input().split())))

direction = [0,1,2,3] #북 동 남 서
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def turn(dir) :
    return (dir -1)%4
check = 0

while True :
    if not visited[r][c] and array[r][c] == 0 :
        visited[r][c] = 1
    dir = turn(dir)
    nr = r + dx[dir]
    nc = c + dy[dir]
    if -1<nr<n and -1<nc<m :
        if array[nr][nc] == 0 and not visited[nr][nc] :
            r,c= nr,nc
            visited[r][c] = 1
            check = 0
            continue
        else :
            check += 1
        if check == 4  :
            nr = r - dx[dir]
            nc = c - dy[dir]
            if array[nr][nc] == 0  :
                r,c = nr,nc
                check = 0
            else :
                break

cnt = 0
for i in range(n) :
    for j in range(m) :
        if visited[i][j] == 1 :
            cnt += 1
print(cnt)


