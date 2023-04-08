
n = int(input())
array = list(map(int,input().split()))
stack = []
stack.append((0,array[0]))
temp = [0]*len(array)
for i in range(1,len(array)) :
    if stack[-1][1] > array[i] :
        stack.append((i,array[i]))
    else :
        while stack[-1][1]<array[i] :
            idx, value = stack.pop()
            temp[idx] = array[i]
            if len(stack) == 0 :
                break
        stack.append((i,array[i]))
while stack :
    idx, value= stack.pop()
    temp[idx] = -1

for i in range(len(temp)) :
    print(temp[i],end=" ")

