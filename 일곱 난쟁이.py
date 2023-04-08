array = []
for _ in range(9) :
    a = int(input())
    array.append(a)
check = True
for i in range(9) :
    first=array[i]
    for j in range(9) :
        if array[i] != array[j] :
            second = array[j]
            if sum(array) - (first+second) == 100 :
                array.remove(first)
                array.remove(second)
                check = False
                break
    if check == False :
        break
array.sort()
for i in range(len(array)) :
    print(array[i])

