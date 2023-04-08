n,m =map(int,input().split())
array= list(map(int,input().split()))
result = []
array.sort()
def recur(x) :
    if len(result) == m :
        print(" ".join(map(str,result)))
        return
    for i in range(x,n) :
        result.append(array[i])
        recur(i)
        result.pop()
recur(0)