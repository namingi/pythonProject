
n = int(input())
array = []

for i in range(n) :
    array.append(list(map(int,input().split())))

line_up = [0,0,0,0,0,0,0,0,0]
visited = [0 for _ in range(9)]
visited[3] = 1
line_up[3] = 0
answer= 0
def recrusive(tmp) :
    global answer
    if tmp == 9 :
        idx = 0
        score = 0
        for inning in array:
            out, b1, b2, b3 = 0, 0, 0, 0
            while out <= 2:
                batter = line_up[idx]
                if inning[batter] == 0:
                    out += 1
                elif inning[batter] == 1:
                    score += b3
                    b1, b2, b3 = 1, b1, b2
                elif inning[batter] == 2:
                    score += b2
                    score += b3
                    b1, b2, b3 = 0, 1, b1
                elif inning[batter] == 3:
                    score += b3
                    score += b1
                    score += b2
                    b1, b2, b3 = 0, 0, 1
                else:
                    score += b1
                    score += b2
                    score += b3
                    score += 1
                    b1, b2, b3 = 0, 0, 0
                idx += 1
                idx = idx % 9
        answer = max(score,answer)
        return
    for i in range(9) :
        if not visited[i]:
            visited[i] =1
            line_up[i] = tmp
            recrusive(tmp+1)
            line_up[i] = 0
            visited[i] = 0

recrusive(1)
print(answer)