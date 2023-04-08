n = int(input())
array = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n) :
    array[i] = list(map(int,input().split()))
result_zero, result_minus,result_one = 0,0,0
def recur(n,x,y) :
    global result_zero,result_minus,result_one
    now = array[x][y]
    for i in range(x,x+n) :
        for j in range(y,y+n) :
            if now != array[i][j] :
                size= n//3
                recur(size,x,y)
                recur(size,x+size,y)
                recur(size,x+2*size,y)
                recur(size,x,y+size)
                recur(size,x,y+2*size)
                recur(size,x+size,y+size)
                recur(size,x+2*size,y+size)
                recur(size,x+size,y+2*size)
                recur(size,x+2*size,y+2*size)
                return
    if now == -1 :
        result_minus+=1
    elif now == 0 :
        result_zero += 1
    elif now == 1 :
        result_one += 1
    return
recur(n,0,0)
print(result_minus)
print(result_zero)
print(result_one)