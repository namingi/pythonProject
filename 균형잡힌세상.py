
while True :
    array = list(map(str, input()))
    stack = []
    if array[0] == "." :
        break
    for i in range(len(array)) :
        if array[i] == "(" :
            stack.append(array[i])
        elif array[i] == "[" :
            stack.append(array[i])
        elif array[i] == ")" :
            if len(stack)>0 and stack[-1] == "(" :
                stack.pop()
            else :
                stack.append(")")
        elif array[i] == "]" :
            if len(stack)>0 and stack[-1] == "[" :
                stack.pop()
            else :
                stack.append("]")
        elif array[i] == " " :
            continue
    if len(stack) == 0 :
        print("yes")
    else :
        print("no")
