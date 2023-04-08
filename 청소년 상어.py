import sys
import copy

input = sys.stdin.readline

def fish_move(gra,shark_idx,fish_num):
  graph = copy.deepcopy(gra)
  for i in range(4):
    for j in range(4):
      if graph[i][j][0] == fish_num:
        num,dir = graph[i][j]
        for k in range(8):
          new_dir = (dir+k)%8
          nx,ny = i+dx[new_dir],j+dy[new_dir]
          if 0>nx or nx>=4 or 0>ny or ny>=4:
            continue
          if shark_idx == [nx,ny]:
            continue
          nnum,ndir = graph[nx][ny]
          graph[nx][ny] = [num,new_dir]
          graph[i][j] = [nnum,ndir]
          return graph
  return graph

def shark_move(graph, shark_idx, fish_total):
  global ans
  for fish_num in range(1,17):
    graph = fish_move(graph, shark_idx, fish_num)
  shark_dir = graph[shark_idx[0]][shark_idx[1]][1]
  for i in range(1,4):
    sx,sy = shark_idx[0]+i*dx[shark_dir],shark_idx[1]+i*dy[shark_dir]
    if 0>sx or sx>=4 or 0>sy or sy>=4:
      continue
    if graph[sx][sy][0] == 0:
      continue
    feed,dir = graph[sx][sy]
    graph[sx][sy][0] = 0
    shark_move(graph,[sx,sy],fish_total+feed)
    graph[sx][sy][0] = feed
  ans = max(ans,fish_total)
  return

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]
graph = [[[0,0] for _ in range(4)] for _ in range(4)]
for i in range(4):
  arr = list(map(int,input().split()))
  for j in range(4):
    graph[i][j][0] = arr[2*j]
    graph[i][j][1] = arr[2*j+1]-1
shark_idx = [0,0]
fish_total = graph[0][0][0]
graph[0][0][0] = 0
ans = 0

shark_move(graph,shark_idx,fish_total)
print(ans)