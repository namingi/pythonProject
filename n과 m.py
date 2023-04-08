n,m = map(int,input().split())
array = []
visited = [0]*n
def recursive(cnt) :
    if len(array) == m :
        print(" ".join(map(str,array)))
        return
    else :
        for i in range(cnt,n) :
            array.append(i+1)
            recursive(i)
            array.pop()


recursive(0)