R,C,M = map(int,input().split())
shark = []
visited = [[ [] for _ in range(C)] for _ in range(R)]
for _ in range(M) :
    r,c,s,d,z = map(int,input().split())
    shark.append([r-1,c-1,s,d-1,z])
    visited[r-1][c-1].append([s,d-1,z])
direction = [0,1,2,3]
dx = [-1,1,0,0]
dy = [0,0,1,-1]

def change(dir) :
    if dir == 0 :
        dir = 1
    elif dir == 1 :
        dir = 0
    elif dir == 2 :
        dir = 3
    elif dir == 3 :
        dir = 2
    return dir
idx = 0
value = 0
while True :
    if idx>=C :
        break
    for i in range(R) :
        if len(visited[i][idx]) != 0 :
            result = visited[i][idx].pop()
            tmp = [i,idx]
            tmp.extend(result)
            value += result[2]
            shark.remove(tmp)
            break
        else :
            continue

    for i in range(len(shark)) :
        x,y,velocity,direction,size = shark[i]
        cnt = 0
        visited[x][y].pop(0)
        while cnt <= velocity-1 :
            nx = x + dx[direction]
            ny = y + dy[direction]
            cnt += 1
            if nx<0 or ny<0 or nx>=R or ny>=C :
                direction = change(direction)
                nx,ny = x + dx[direction], y + dy[direction]
            x,y = nx,ny
        shark[i] = [x,y,velocity,direction,size]
        visited[x][y].append([velocity,direction,size])
    for x in range(R) :
        for y in range(C) :
            if len(visited[x][y]) >=2 :
                visited[x][y].sort(key = lambda x : x[2])
                while True :
                    if len(visited[x][y]) == 1 :
                        break
                    result = visited[x][y].pop(0)
                    tmp = [x,y]
                    tmp.extend(result)
                    shark.remove(tmp)
    idx += 1

print(value)