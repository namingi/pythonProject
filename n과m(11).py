n,m = map(int,input().split())
array = list(map(int,input().split()))
result = []
array.sort()
def recur(x):
    if len(result) == m :
        print(" ".join(map(str,result)))
        return
    tmp = 0
    for i in range(n) :
        if tmp != array[i] :
            result.append(array[i])
            tmp = array[i]
            recur(x+1)
            result.pop()
recur(0)



