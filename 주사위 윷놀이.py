import copy
board = [[i for i in range(0, 42, 2)],
         [10, 13, 16, 19, 25, 30, 35, 40],
         [20, 22, 24, 25, 30, 35, 40],
         [30, 28, 27, 26, 25, 30, 35, 40]]
pos = [[i for i in range(21)],
       [5, 21, 22, 23, 24, 25, 26, 20],
       [10, 27, 28, 24, 25, 26, 20],
       [15, 29, 30, 31, 24, 25, 26, 20]]
array = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2]
move = [0 for _ in range(10)]
answer = 0
def recursive(idx) :
    if idx == 10 :
        score(move)
        return
    for i in range(4) :
        move[idx] = i
        recursive(idx + 1)
        move[idx] -= i
result = 0
def score(move) :
    global result
    horse = [[0, 0] for _ in range(4)]
    sum_val = 0
    for i in range(len(move)) :
         now = move[i]
         x,y = horse[now]
         if x == -1  :
             return
         y += array[i]
         if x == 0 :
             if y>=len(board[x]) :
                 horse[now] = [-1,-1]
             elif y == 5 :
                 horse[now] = [1,0]
             elif y == 10 :
                 horse[now] = [2,0]
             elif y == 15 :
                 horse[now] = [3,0]
         else :
             if y>= len(board[x]) :
                 horse[now] = [-1,-1]
             else :
                 horse[now] = x,y
         nx,ny = horse[now]
         if nx != -1 :
             for h in range(4) :
                 na,nb = horse[h]
                 if na == -1 :
                     continue
                 if now == h :
                     continue
                 if pos[na][nb] == pos[nx][ny] :
                     return
             sum_val += board[nx][ny]
    result = max(sum_val,result)




