n = int(input())
array = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n) :
    array[i] = list(map(int,input()))
result = []

def recur(n,x,y) :
    now=array[x][y]
    global result
    for i in range(x,x+n) :
        for j in range(y,y+n) :
            if now != array[i][j] :
                size = n//2
                result.append("(")
                recur(size,x,y)
                recur(size,x,y+size)
                recur(size,x+size,y)
                recur(size,x+size,y+size)
                result.append(")")
                return
    if now == 0 :
        result.append("0")
    else :
        result.append("1")
    return
recur(n,0,0)
print("".join(map(str,(result))))