import sys
from copy import deepcopy

n, m, k = map(int, input().rstrip('\n').split())

fireball = [[[] for _ in range(n)] for _ in range(n)]

for _ in range(m):
	r, c, m, s, d = map(int, input().rstrip('\n').split())
	fireball[r-1][c-1].append([m, s, d])

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(k):
	board = [[[] for _ in range(n)] for _ in range(n)]

	# 1. 파이어볼의 이동
	for i in range(n):
		for j in range(n):
			if fireball[i][j]:
				for dir in range(len(fireball[i][j])):
					nm, ns, nd = fireball[i][j][dir]
					nx = i + (dx[nd] * ns)
					ny = j + (dy[nd] * ns)

					nx = (nx + n) % n
					ny = (ny + n) % n
					board[nx][ny].append([nm, ns, nd])

	# 2. 2개 이상의 파이어볼이 있는 칸에서는 다음과 같은 일이 일어난다.
	for i in range(n):
		for j in range(n):
			if len(board[i][j]) > 1:
				cm, cs, cd = 0, 0, []
				length = len(board[i][j])

				for e in range(length):
					cm += board[i][j][e][0]
					cs += board[i][j][e][1]
					cd.append(board[i][j][e][2] % 2)

				cm = int(cm / 5)
				cs = int(cs / length)
				board[i][j] = []

				if cm != 0:
					if sum(cd) == 0 or sum(cd) == length:
						for idx in range(4):
							board[i][j].append([cm, cs, idx * 2])
					else:
						for idx in range(4):
							board[i][j].append([cm, cs, idx * 2 + 1])

	fireball = deepcopy(board)

res = 0

#결과 출력
for i in range(n):
	for j in range(n):
		if fireball[i][j]:
			for ball in range(len(fireball[i][j])):
				res += fireball[i][j][ball][0]

print(res)