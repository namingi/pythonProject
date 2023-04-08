array = []
for i in range(7) :
    a = int(input())
    if a%2 != 0 :
        array.append(a)
if len(array) == 0 :
    print(-1)
else :
    print(sum(array))
    print(min(array))