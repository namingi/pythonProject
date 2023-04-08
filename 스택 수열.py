n = int(input())

stack= []
flag = True
count = 1
result = []
for _ in range(n) :
    num = int(input())
    while count <=num :
        result.append("+")
        stack.append(count)
        count += 1
    if stack[-1] == num :
        result.append("-")
        stack.pop()
    elif stack[-1] >num :
        flag = False

if flag == False :
    print("NO")
else :
   for i in range(len(result)) :
       print(result[i])


