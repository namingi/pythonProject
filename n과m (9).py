import sys
n,m = map(int,sys.stdin.readline().split())
array = list(map(int,sys.stdin.readline().split()))
result = []
array.sort()
visited = [0]*n
def recur() :
    if len(result) == m :
        print(" ".join(map(str,result)))
        return
    tmp = 0
    for i in range(n) :
        if tmp != array[i] and not visited[i] :
            visited[i] = 1
            result.append(array[i])
            tmp = array[i]
            recur()
            result.pop()
            visited[i] = 0
recur()
