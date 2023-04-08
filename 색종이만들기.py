n = int(input())
array = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n) :
    array[i] = list(map(int,input().split()))
result,value = 0,0
def recur(n,x,y) :
    global result
    global value
    now = array[x][y]
    for i in range(x,x+n) :
        for j in range(y,y+n) :
            if array[i][j] != now :
                size = n//2
                recur(size,x,y)
                recur(size,x+size,y)
                recur(size,x,y+size)
                recur(size,x+size,y+size)
                return

    if now == 1 :
        result +=1
    else :
        value +=1
    return
recur(n,0,0)
print(value)
print(result)
