n = int(input())
array = []
for _ in range(n) :
    array.append(int(input()))

stack = []
result = 0
stack.append(array[0])
for i in range(1,len(array)) :
    if stack[-1] > array[i] :
        result += len(stack)
        stack.append(array[i])
    else :
        while stack[-1] <= array[i] :
            stack.pop()
            if len(stack) == 0 :
                break
        if stack[-1] > array[i] :
            result += len(stack)
        stack.append(array[i])
print(result)