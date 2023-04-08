def recur(x) :
    if len(result) == 6 :
        print(" ".join(map(str,result)))
        return

    for i in range(x,len(array)) :
        if not visited[i] :
            visited[i] = 1
            result.append(array[i])
            recur(i+1)
            visited[i] = 0
            result.pop()


while True :
    array = list(map(int,input().split()))
    n = array[0]
    result = []
    visited = [0]*n
    if n == 0 :
        break
    array.pop(0)
    array.sort()
    recur(0)
    print()
