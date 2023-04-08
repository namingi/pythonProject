
N,X = map(int,input().split())
A = list(map(int,input().split()))
for i in range(len(A)) :
    if A[i]<X :
        print(A[i],end=" ")

        for i in range(len(array)):
            for j in range(len(array[i])):
                if len(array[i][j]) >= 2:
                    length = len(array[i][j])
                    weight = 0
                    speed = 0
                    direction = 0
                    for k in range(len(array[i][j])):
                        ww, ss, dd = array[i][j].pop(0)
                        weight += ww
                        speed += ss
                        direction += dd
                    weight = int(weight / 5)
                    speed = int(speed / length)
                    direction = int(direction)
                    for m in range(4):
                        if direction % 2 == 0 and weight != 0:
                            fire.append([i, j, weight, speed, 2 * m])
                            array[i][j].append([weight, speed, 2 * m])
                        elif direction % 2 != 0 and weight != 0:
                            fire.append([i, j, weight, speed, 2 * m + 1])
                            array[i][j].append([weight, speed, 2 * m + 1])