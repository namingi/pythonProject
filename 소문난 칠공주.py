from collections import deque
array = []
for i in range(5) :
    array.append(list(map(str,input())))
visited =[0 for _ in range(25)]

def four() :
    cnt = 0
    for i in range(25) :
        if visited[i] == 1 :
            x = i%5
            y = i//5
            if array[x][y] == "S" :
                cnt += 1
    if cnt >= 4 :
        return True
    else :
        return False
dx = [-1,0,1,0]
dy = [0,1,0,-1]
def adjacency() :
    size = 1
    queue = deque ()
    check_visited = [[0 for _ in range(5)] for _ in range(5)]
    queue_visited = [[0 for _ in range(5)] for _ in range(5)]
    for i in range(25) :
        if visited[i] == 1 :
            x = i//5
            y = i%5
            check_visited[x][y] = 1
            if len(queue) == 0 :
                queue.append((x,y))
                queue_visited[x][y] = 1

    while queue :
        x,y = queue.popleft()
        if size == 7 :
            return True
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if -1<nx<5 and -1<ny<5 :
                if check_visited[nx][ny] == 1 and queue_visited[nx][ny] == 0 :
                    queue.append((nx,ny))
                    queue_visited[nx][ny] = 1
                    size += 1
    return False


ans = 0
def recur(idx,cnt) :
    global ans
    if cnt == 7 :
        if four() == True :
            if adjacency() == True :
                ans +=1
        return
    for i in range(idx,25) :
        if not visited[i] :
            visited[i] = 1
            recur(i,cnt+1)
            visited[i] = 0

recur(0,0)
print(ans)