n = int(input())
array = [[" " for _ in range(4*n-3) ] for _ in range(4*n-1)]

def star(n,x,y) :
    if n == 1 :
        array[x][y] = "*"
        array[x+1][y] = "*"
        array[x+2][y] = "*"
        return
    else:
        for i in range(4*n-4) :
            array[x][y] = "*"
            y -=1
        for j in range(4*n-2) :
            array[x][y] = "*"
            x +=1
        for i in range(4*n-4) :
            array[x][y] = "*"
            y+=1
        for j in range(4*n-4) :
            array[x][y] = "*"
            x-=1

        array[x][y] = "*"
        array[x][y-1] = "*"
        star(n-1,x,y-2)



star(n,0,4*n-4)
if n == 1 :
    print("*")
else :
    for s in array :
        print("".join(s).rstrip())