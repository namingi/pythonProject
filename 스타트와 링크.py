n = int(input())
array = []
for _ in range(n) :
    array.append(list(map(int,input().split())))
visited = [0 for _ in range(n)]
answer= 9999
def recursive(tmp,idx) :
    global answer
    if tmp == n/2 :
        value = sum(visited)
        answer= min(value,answer)
        return
    for i in range(idx,len(visited)):
        if not visited[i] :
            visited[i] = 1
            recursive(tmp+1,i+1)
            visited[i] = 0
def sum(visited) :
    sum = 0
    sum_2 = 0
    for i in range(n) :
        if visited[i] == 1 :
            for j in range(n) :
                if visited[j] == 1 :
                    if i !=j :
                        sum += array[i][j]
    for i in range(n) :
        if visited[i] == 0 :
            for j in range(n) :
                if visited[j] == 0 :
                    if i!=j :
                        sum_2 +=array[i][j]

    return abs(sum-sum_2)
recursive(0,0)
print(answer)