k = int(input())
array = []
for _ in range(k) :
    num = int(input())
    if num == 0 :
        array.pop()
    else :
        array.append(num)
print(sum(array))
