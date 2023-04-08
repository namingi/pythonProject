n = int(input())
array = []
for i in range(n) :
    a,b= map(int,input().split())
    array.append([a,b])
tmp = 0
value = 0
def recur(x) :
    global value
    global tmp
    if x == n :
        value = max(value,tmp)
        return
    if array[x][0] <= 0 or tmp == n-1  :
        recur(x+1)
        return
    for j in range(n) :
        if j == x or array[j][0] <=0 :
            continue
        array[x][0] -=array[j][1]
        array[j][0] -=array[x][1]
        if array[x][0] <= 0 :
            tmp += 1
        if array[j][0] <= 0 :
            tmp += 1
        recur(x+1)
        if array[x][0] <= 0 :
            tmp -= 1
        if array[j][0] <= 0 :
            tmp -= 1
        array[x][0] += array[j][1]
        array[j][0] += array[x][1]
recur(0)
print(value)


