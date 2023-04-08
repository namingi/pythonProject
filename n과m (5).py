n,m = map(int,input().split())
array = list(map(int,input().split()))
array.sort()
result = []
visited = [0]*(n)
def recur(cnt) :
    if len(result) == m :
        print(" ".join(map(str,result)))
        return
    for i in range(cnt,n) :
        if not visited[i] :
            visited[i] = 1
            result.append(array[i])
            recur(i+1)
            result.pop()
            visited[i] = 0
recur(0)


