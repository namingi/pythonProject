n = int(input())

stack = []
result = 0
for i in range(n) :
    m = int(input())
    cnt = 1
    while stack and stack[-1][1]<=m :
        index, now = stack.pop()
        result += index
        if m == now :
           cnt += index

    if stack :
        result += 1
    stack.append((cnt,m))
print(result)



