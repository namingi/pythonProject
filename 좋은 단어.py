n = int(input())
result = 0
for _ in range(n) :
    array = list(map(str, input()))
    stack = []
    for i in range(len(array)) :
        if array[i] == "A" :
            if len(stack) == 0 :
                stack.append(array[i])
            else :
                if stack[-1] == "A" :
                    stack.pop()
                else :
                    stack.append(array[i])
        elif array[i] == "B" :
            if len(stack) == 0 :
                stack.append(array[i])
            else :
                if stack[-1] == "B" :
                    stack.pop()
                else :
                    stack.append(array[i])
    if len(stack) == 0 :
        result += 1
print(result)
