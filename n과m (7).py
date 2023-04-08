n,m = map(int,input().split())
array = list(map(int,input().split()))
result = []
def recur(x) :
    if len(result) == m :
        print(" ".join(map(str,result)))
        return
    for i in range(n) :
        result.append(array[i])
        recur(x+1)
        result.pop()
array.sort()
recur(0)
