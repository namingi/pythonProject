
n = int(input())
array = list(map(int,input().split()))
add,sub,mul,div = map(int,input().split())

max_answer = -9999
min_answer = 9999
def dfs(i,now) :
    global min_answer,max_answer,add,sub,mul,div
    if i == n :
        min_answer = min(min_answer,now)
        max_answer = max(max_answer,now)
    else :
        if add>0 :
            add -= 1
            dfs(i+1,now+array[i])
            add += 1
        if sub > 0 :
            sub -= 1
            dfs(i+1,now - array[i])
            sub +=1
        if mul>0 :
            mul -= 1
            dfs(i+1,now*array[i])
            mul+=1
        if div >0 :
            div -= 1
            dfs(i+1,int(now/array[i]))
            div += 1
dfs(1,array[0])
print(max_answer)
print(min_answer)

