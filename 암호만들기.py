n,m = map(int,input().split())
array = list(map(str,input().split()))
array.sort()
result = []
visited = [0]*(m)
def recur(x,aeiou,etc) :
    if len(result) == n and aeiou>=1 and etc>=2 :
        print("".join(map(str,result)))
        return

    for i in range(x,m) :
        if array[i] == "a" or array[i] == "i" or array[i] == "e" or array[i] == "o" or array[i] == "u" :
            if not visited[i] :
                visited[i] = 1
                result.append(array[i])
                recur(i+1,aeiou+1,etc)
                result.pop()
                visited[i] = 0
        else :
            if not visited[i] :
                visited[i] = 1
                result.append(array[i])
                recur(i+1,aeiou,etc+1)
                result.pop()
                visited[i] = 0
recur(0,0,0)
