n,k = map(int,input().split())
move = [0 for _ in range(n)]
visited = [0 for _ in range(n)]
array = []
for _ in range(n) :
    array.append(list(map(int,input().split())))
second = list(map(int,input().split()))
third = list(map(int,input().split()))
result = -1
def recursive(idx) :
    global result
    if idx == n :
        result = max(win(move),result)
        return
    for i in range(len(move)) :
        if not visited[i] :
            visited[i] = 1
            move[idx] = i+1
            recursive(idx+1)
            move[idx] -= i+1
            visited[i] = 0
def win(move) :
    cnt = [0,0,0]
    person = [0,1,2]
    flag = False
    first_idx,second_idx,third_idx = 0,0,0
    a,b = 0,1
    while True :
        if cnt[1] == k or cnt[2] == k :
            break
        elif cnt[0] == k :
            flag = True
            break
        if first_idx >= n :
            break

        if a == 0 and b == 1 :
            if array[move[first_idx]-1][second[second_idx]-1] == 2 :
                cnt[a] += 1
                a= 0
                b = 2
            elif array[move[first_idx]-1][second[second_idx]-1] == 1 :
                cnt[b] += 1
                a= 1
                b= 2
            else :
                cnt[b] += 1
                a = 1
                b = 2
            first_idx += 1
            second_idx += 1
        elif a == 0 and b == 2 :
            if array[move[first_idx] - 1][third[third_idx] - 1] == 2:
                cnt[a] +=1
                a= 0
                b = 1
            elif array[move[first_idx] - 1][third[third_idx] - 1] == 1:
                cnt[b] += 1
                a = 1
                b = 2
            else :
                cnt[b] += 1
                a = 1
                b= 2
            first_idx+=1
            third_idx += 1
        elif a == 1 and b == 2 :
            if array[second[second_idx] - 1][third[third_idx] - 1] == 2:
                cnt[a] += 1
                a = 0
                b = 1
            elif array[second[second_idx] - 1][third[third_idx] - 1] == 1:
                cnt[b] += 1
                a= 0
                b= 2
            else :
                cnt[b] += 1
                a = 0
                b = 2
            second_idx += 1
            third_idx += 1
    if flag :
        return 1
    else :
        return 0

recursive(0)
print(result)