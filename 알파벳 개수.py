s = str(input())

s = list(s)
array = "abcdefghijklmnopqrstuvwxyz"
array = list(array)
board = [0]*26
for i in range(len(s)) :
    for j in range(len(array)) :
        if array[j] == s[i] :
            board[j] += 1

for i in range(len(board)) :
    print(board[i], end =" ")
