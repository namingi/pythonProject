n = int(input())
for _ in range(n) :
    array = list(map(str, input()))
    stack = []
    for i in range(len(array)) :
        if array[i] == "(" :
            stack.append(array[i])
        elif len(stack) > 0 and array[i] == ")":
            if stack[-1] == "(" :
                stack.pop()
        elif len(stack) == 0 and array[i] == ")" :
            stack.append(")")
    if len(stack)==0 :
        print("YES")
    else :
        print("NO")