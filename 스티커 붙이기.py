def is_attachable(board,start_x,start_y) :
  flag = True
  for i in range(start_x,start_x+r) :
    for j in range(start_y,start_y+c) :
      if -1<i<n and -1<j<m :
        if array[i][j]== 0 :
          flag = True
        elif array[i][j] == 1 and board[i-start_x][j-start_y] == 0 :
          flag = True
        elif array[i][j] == 1 and board[i-start_x][j-start_y] == 1 :
          flag = False
          return flag
      else :
        flag = False
        return flag
  return flag

def attach(board,start_x,start_y) :
  for i in range(start_x,start_x+r) :
    for j in range(start_y,start_y+c) :
      array[i][j] += board[i-start_x][j-start_y]

def rotate_90(board,r,c) :
  array_1 = [[0 for _ in range(r)] for _ in range(c)]
  for i in range(c) :
    for j in range(r) :
      array_1[i][j] = board[r-j-1][i]
  return array_1

n,m,k = map(int,input().split())
array = [[0 for _ in range(m)] for _ in range(n)]
for a in range(k) :
  r,c = map(int,input().split())
  board = [list(map(int,input().split())) for _ in range(r)]
  do = False
  for s in range(4) :
    for i in range(n) :
      for j in range(m) :
        if is_attachable(board,i,j) :
          attach(board,i,j)
          do = True
          break
      if do :
        break
    if do :
      break
    else :
      board,r,c = rotate_90(board,r,c),c,r
cnt = 0
for i in range(len(array)) :
    for j in range(len(array[0])) :
        if array[i][j] == 1 :
            cnt += 1
print(cnt)