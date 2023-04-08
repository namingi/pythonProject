
n = int(input())
stars = [[" " for _ in range(n)] for _ in range(n)]
def star(n,x,y) :
    if n == 1 :
        stars[x][y] = "*"
        return
    else :
        for i in range(3) :
            for j in range(3) :
                if i==1 and j==1 :
                    continue
                star(n//3,x+n//3*i,y+n//3*j)

star(n,0,0)
for k in stars :
    print("".join(k))