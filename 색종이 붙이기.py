array = []
for _ in range(10) :
    array.append(list(map(int,input().split())))

def check(x,y,size) :
    if x + size > 10 or y+size > 10 :
        return False
    for i in range(x,x+size) :
        for j in range(y,y+size) :
            if array[i][j] != 1 :
                return False
    return True

count = [5,5,5,5,5]
min_cnt = 31
def recursive(depth,cnt) :
    global min_cnt
    if depth >= 100 :
        min_cnt = min(min_cnt,cnt)
        return
    if cnt >= min_cnt :
        return

    row = depth//10
    col = depth%10
    if array[row][col] == 1 :
        for i in range(1,6) :
            if check(row,col,i) :
                if count[i-1] == 0 :
                    continue
                attatch(row,col,i,True)
                count[i-1] -=1
                recursive(depth+1,cnt+1)
                count[i-1] +=1
                attatch(row,col,i,False)
    else :
        recursive(depth+1,cnt)


def attatch(row,col,size,flag) :
    if flag == True :
        for i in range(row,row+size) :
            for j in range(col,col+size) :
                if array[i][j] == 1 :
                    array[i][j] = 0
    else :
        for i in range(row,row+size) :
            for j in range(col,col+size) :
                if array[i][j] == 0 :
                    array[i][j] = 1

recursive(0,0)
if min_cnt == 31 :
    print(-1)
else :
    print(min_cnt)