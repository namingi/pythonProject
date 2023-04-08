from collections import deque
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def recursive(idx) :
    if idx == len(dust) :
        score()
        return
    for i in range(len(dust)) :
        if not check[i] :
            board.append(i)
            check[i] = 1
            recursive(idx+1)
            check[i] = 0
            board.pop()

def score() :
    global answer
    temp = cleaner[board[0]]
    start = board[0]
    for i in range(1,len(board)) :
        end = board[i]
        temp += dists[start][end]
        start = end
    answer = min(answer,temp)

def bfs(i,j) :
    queue = deque()
    queue.append((i,j))
    visited =[[-1 for _ in range(w)] for _ in range(h)]
    visited[i][j] = 0
    while queue :
        x,y = queue.popleft()
        for i in range(4) :
            nx =x + dx[i]
            ny = y + dy[i]
            if -1<nx<h and -1<ny<w :
                if array[nx][ny] != "x" :
                    if visited[nx][ny] == -1 :
                        visited[nx][ny] = visited[x][y] + 1
                        queue.append((nx,ny))
    return visited

while True :
    w,h = map(int,input().split())
    if w == 0 and h == 0 :
        break
    else :
        array = []
        dust = []
        board = []
        answer = 9999
        for _ in range(h) :
            array.append(list(map(str,input())))
        for i in range(h) :
            for j in range(w) :
                if array[i][j] == "o" :
                    sx,sy = i,j
                if array[i][j] == "*" :
                    dust.append((i,j))
        distance = bfs(sx,sy)
        cleaner = [0]*(len(dust))
        flag = True
        check = [0 for _ in range(len(dust))]
        for i in range(len(dust)) :
            temp = distance[dust[i][0]][dust[i][1]]
            if temp == -1 :
                flag = False
                answer= -1
                break
            cleaner[i] += temp
        if flag :
            dists = [[0 for _ in range(len(dust))] for _ in range(len(dust))]
            for i in range(len(dust)-1) :
                dis = bfs(dust[i][0],dust[i][1])
                for j in range(i+1,len(dust)) :
                    dists[i][j] = dis[dust[j][0]][dust[j][1]]
                    dists[j][i] = dists[i][j]
            recursive(0)
        print(answer)
