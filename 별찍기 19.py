n = int(input())
array = [[" " for _ in range(4*n-3)]for _ in range(4*n-3)]
def recur(n,x,y) :
    if n == 1 :
        array[x][y] = "*"
        return
    else :
        length = 4*n-3
        for i in range(length) :
            array[x][y+i] = "*"
            array[x+i][y] = "*"
            array[x+length-1][y+i] = "*"
            array[x+i][y+length-1] = "*"
        recur(n-1,x+2,y+2)
recur(n,0,0)

for s in array :
    print("".join(s))