n = int(input())
stars = [[" " for _ in range(2*n)] for _ in range(n)]

def star(n,x,y) :
    if n == 3 :
        stars[x][y] ="*"
        stars[x+1][y-1] = "*"
        stars[x+1][y+1] = "*"
        for i in range(-2,3) :
            stars[x+2][y+i] = "*"
        return
    else :
        star(n//2,x,y)
        star(n//2,x+n//2,y-n//2)
        star(n//2,x+n//2,y+n//2)

star(n,0,n-1)
for row in stars :
    print("".join(row))