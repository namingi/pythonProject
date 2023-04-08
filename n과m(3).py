n,m = list(map(int,input().split()))

array = []
def recur() :
    if len(array) == m :
        print(" ".join(map(str,array)))
        return
    for i in range(1,n+1) :
        array.append(i)
        recur()
        array.pop()
recur()