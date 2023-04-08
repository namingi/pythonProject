n,m,h  = map(int,input().split())
array = [[0 for _ in range(n)]for _ in range(h)]
for _ in range(m) :
    a,b = map(int,input().split())
    array[a-1][b-1] = 1
def down() :
    for start in range(n) :
        y = start
        for i in range(h) :
            if array[i][y] == 1 :
                y+=1
            elif array[i][y-1] == 1 :
                y-=1
        if y!=start :
            return False
    return True

ans = 4
def recursive(cnt) :
    global ans
    if down() :
        ans = min(ans,cnt)
        return
    elif cnt == 3 or ans<=cnt :
        return
    for i in range(h) :
       for j in range(n-1) :
           if array[i][j] == 1 :
               continue
           elif j-1>=0 and array[i][j-1] ==1 :
               continue
           elif j+1<n and array[i][j+1] == 1 :
               continue
           array[i][j] = 1
           recursive(cnt+1)
           array[i][j] = 0
recursive(0)
if ans <4 :
    print(ans)
else :
    print(-1)