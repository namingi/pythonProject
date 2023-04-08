array = list(map(str,input()))
stack = []
laser = 0
result = 0
check = False
for i in range(len(array)) :
    if array[i] == "(" :
        stack.append(array[i])
    elif array[i] == ")" :
        if len(stack) > 0 and array[i-1] == "(" :
            stack.pop()
            laser = 1
            if len(stack) == 0 :
                laser = 0
            else :
                result += laser*len(stack)
        elif array[i-1] == ")" :
            stack.pop()
            result +=1
print(result)