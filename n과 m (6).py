n,m = map(int,input().split())
array = list(map(int,input().split()))
result = []
def recur(x) :
    if len(result) == m :
        print(" ".join(map(str,result)))
    for i in range(x,n) :
        result.append(array[i])
        recur(i+1)
        result.pop()
array.sort()
recur(0)

