n,l = map(int,input().split())
array = []
sum = 0
for _ in range(n) :
    array.append(list(map(int,input().split())))
for j in range(n) :
    flag = True
    visited = [0 for _ in range(n)]
    for i in range(n-1) :
        if array[i][j] == array[i+1][j] :
            continue
        elif array[i][j] ==  array[i+1][j] + 1  :
            for k in range(i+1,i+l+1) :
                if 0<=k<n :
                    if array[k][j] != array[i+1][j] :
                        flag = False
                    if visited[k] :
                        flag= False
                    visited[k] = 1
                else :
                    flag= False
        elif array[i][j] + 1 == array[i+1][j] :
            for k in range(i,i-l,-1) :
                if 0<=k<n :
                    if array[k][j] != array[i][j] :
                        flag = False
                    if visited[k] :
                        flag= False
                    visited[k] = 1
                else :
                    flag= False
        else :
            flag= False
    if flag == True :
        sum += 1
    else :
        sum += 0

for i in range(n) :
    flag = True
    visited = [0 for _ in range(n)]
    for j in range(n-1) :
        if array[i][j] == array[i][j+1] :
            continue
        elif array[i][j] ==  array[i][j+1] + 1  :
            for k in range(j+1,j+l+1) :
                if 0<=k<n :
                    if array[i][k] != array[i][j+1] :
                        flag = False
                    if visited[k] :
                        flag= False
                    visited[k] = 1
                else :
                    flag= False
        elif array[i][j] + 1 == array[i][j+1] :
            for k in range(j,j-l,-1) :
                if 0<=k<n :
                    if array[i][k] != array[i][j] :
                        flag = False
                    if visited[k] :
                        flag= False
                    visited[k] = 1
                else :
                    flag= False
        else :
            flag= False
    if flag == True :
        sum += 1
    else :
        sum += 0


print(sum)