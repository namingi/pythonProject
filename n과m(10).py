n,m = map(int,input().split())
array = list(map(int,input().split()))
result = []
visited = [0]*n
array.sort()
def recur(x) :
    if len(result) == m :
        print(" ".join(map(str,result)))
        return
    tmp = 0
    for i in range(x,n) :
        if not visited[i] and tmp != array[i] :
            tmp = array[i]
            visited[i] = 1
            result.append(array[i])
            recur(i+1)
            visited[i] = 0
            result.pop()
recur(0)