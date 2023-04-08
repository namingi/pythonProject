n,m = map(int,input().split())
array = []
for i in range(n) :
    array.append(list(map(int,input().split())))
board = []
chicken = []
for i in range(n) :
    for j in range(n) :
        if array[i][j] == 2 :
            chicken.append((i,j))
        if array[i][j] == 1 :
            board.append((i,j))
visited = [0]*len(chicken)
result = []
ans = 9999
def recursive(tmp) :
    global ans
    if len(result) == m :
        value = 9999
        cnt = 0
        for i in range(len(board)) :
            x,y = board[i][0],board[i][1]
            for k in range(len(result)) :
                size = abs(x-result[k][0]) + abs(y-result[k][1])
                value = min(size,value)
            cnt += value
            value =9999
        ans = min(cnt,ans)
        return
    for t in range(tmp,len(chicken)) :
        if not visited[t] :
            visited[t] = 1
            result.append(chicken[t])
            recursive(t+1)
            visited[t] = 0
            result.pop()
recursive(0)
print(ans)