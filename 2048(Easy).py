n = int(input())
array = []
import copy
for i in range(n) :
    array.append(list(map(int,input().split())))
dir = [0,1,2,3]#상 하 좌 우
answer = 0 # 답
def recursive(tmp) :
    global answer
    global array
    if tmp == 5 :
        size = 0
        for i in range(n) :
            for j in range(n) :
                size = max(array[i][j],size)
        answer=max(size,answer)
        return
    board = copy.deepcopy(array)
    for i in range(len(dir)) : # 백트래킹 조건
        move(dir[i])
        recursive(tmp+1)
        array = copy.deepcopy(board)
dx = [-1,1,0,0]
dy = [0,0,-1,1]
result = []
def move(di):
    if di == 0:
        for j in range(n):
            idx = 0
            for i in range(1, n):
                if array[i][j]:
                    temp = array[i][j]
                    array[i][j] = 0
                    if array[idx][j] == 0:
                        array[idx][j] = temp
                    elif array[idx][j] == temp:
                        array[idx][j] = temp * 2
                        idx += 1
                    else:
                        idx += 1
                        array[idx][j] = temp
    elif di == 1:
        for j in range(n):
            idx = n - 1
            for i in range(n - 2, -1, -1):
                if array[i][j]:
                    temp = array[i][j]
                    array[i][j] = 0
                    if array[idx][j] == 0:
                        array[idx][j] = temp
                    elif array[idx][j] == temp:
                        array[idx][j] = temp * 2
                        idx -= 1
                    else:
                        idx -= 1
                        array[idx][j] = temp

    elif di == 2:
        for i in range(n):
            idx = 0
            for j in range(1, n):
                if array[i][j]:
                    temp = array[i][j]
                    array[i][j] = 0
                    if array[i][idx] == 0:
                        array[i][idx] = temp
                    elif array[i][idx] == temp:
                        array[i][idx] = temp * 2
                        idx += 1
                    else:
                        idx += 1
                        array[i][idx] = temp

    else:
        for i in range(n):
            idx = n - 1
            for j in range(n - 2, -1, -1):
                if array[i][j]:
                    temp = array[i][j]
                    array[i][j] = 0
                    if array[i][idx] == 0:
                        array[i][idx] = temp
                    elif array[i][idx] == temp:
                        array[i][idx] = temp * 2
                        idx -= 1
                    else:
                        idx -= 1
                        array[i][idx] = temp

recursive(0)
print(answer)