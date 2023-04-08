n,m = map(int,input().split())
board = []
for i in range(n):
    board.append(list(map(int,input().split())))
dx = [-1,1,0,0]
dy = [0,0,1,-1]
visited = [[0 for _ in range(m)] for _ in range(n)]
result = 0
def dfs(x,y,cnt,value) :
    global result
    if cnt == 4 :
        result= max(result,value)
        return
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if -1<nx<n and -1<ny<m :
            if not visited[nx][ny] :
                visited[nx][ny] = 1
                dfs(nx,ny,cnt+1,value+board[nx][ny])
                visited[nx][ny] = 0

def exec(x,y) :
    global result
    temp = 0
    adj = []
    for i in range(4) :
        if -1<x + dx[i]<n and -1<y+dy[i]<m :
            adj.append(board[x+dx[i]][y+dy[i]])
    if len(adj) >=3 :
        temp = board[x][y] + sum(sorted(adj, reverse=True)[:3])
    result = max(temp,result)

for i in range(n) :
    for j in range(m) :
        visited[i][j] = 1
        dfs(i,j,1,board[i][j])
        exec(i,j)
        visited[i][j] = 0
print(result)