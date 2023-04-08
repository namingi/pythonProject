n,m = map(int,input().split())

array = []
visited = [0]*(n+1)
def recur(x) :
    if len(array) == m :
        print(" ".join(map(str,array)))
        return
    for i in range(x,n+1) :
        array.append(i)
        recur(i+1)
        array.pop()
recur(1)


