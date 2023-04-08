from collections import deque
F,S,G,U,D = map(int,input().split())
queue = deque()
queue.append(S)
visited = [0]*(F+1)
visited[S] = 1
def bfs() :
    String= "use the stairs"
    while queue :
        now = queue.popleft()
        if now == G :
            return visited[G]-1
        if now+U<=F :
            if visited[now+U] == 0 :
                visited[now+U] = 1
                visited[now+U] = visited[now] + 1
                queue.append(now+U)
        if 0<now-D :
            if visited[now-D] == 0 :
                visited[now-D] = 1
                visited[now-D] = visited[now] + 1
                queue.append(now-D)
    return String

print(bfs())

