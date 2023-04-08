n = int(input())
dx = [1,0,-1,0] #0 1 2 3
dy = [0,-1,0,1]

def dragon_curve(x,y,d,g) :
    axis = []
    cnt = 0
    axis.append((x,y))
    x,y = axis[-1][0],axis[-1][1]
    x+= dx[d]
    y+= dy[d]
    axis.append((x,y))
    cnt += 1
answer = 0
visited = [[0 for _ in range(101)]for _ in range(101)]
for i in range(n) :
    x,y,d,g = map(int,input().split())
    direction = []
    direction.append(d)
    axis = []
    axis.append((x,y))
    cnt = 0
    while True :
        if g == 0 :
            break
        cnt += 1
        for i in range(len(direction)-1,-1,-1) :
            dir = direction[i]
            dir = (dir+1)%4
            direction.append(dir)
        if cnt == g :
            break
    for j in range(len(direction)) :
        x += dx[direction[j]]
        y += dy[direction[j]]
        if -1<x<101 and -1<y<101 :
            axis.append((x,y))
    for j in range(len(axis)) :
        visited[axis[j][1]][axis[j][0]] = 1
for i in range(100) :
     for j in range(100) :
         if visited[j][i] == 1 :
             if visited[j][i+1] == 1 and visited[j+1][i] == 1  and visited[j+1][i+1] == 1 :
                 answer +=1
print(answer)
