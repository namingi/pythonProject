n,m = map(int,input().split())
array = list(map(int,input().split()))
value = 0
def recur(x,result) :
    global value
    if x == n :
        return
    result+= array[x]
    if result == m :
        value += 1
    recur(x+1,result)
    recur(x+1,result-array[x])
recur(0,0)
print(value)


