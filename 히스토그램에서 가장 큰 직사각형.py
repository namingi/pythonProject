while True :
    array = list(map(int,input().split()))
    n = array[0]
    if n == 0 :
        break
    array = array[1:]
    stack = []
    result = 0
    for i in range(n) :
        min_point = i
        number = array[i]
        while stack and stack[-1][1]>number :
            min_point, now = stack.pop()
            if result < (i-min_point)*now :
                result = (i-min_point)*now
        stack.append((min_point,number))

    while stack :
        index, now = stack.pop()
        if result < (n-index)*now :
            result = (n-index)*now

    print(result)
