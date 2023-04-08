n = int(input())
array = list(map(int,input().split()))
x = int(input())
result = 0

i = 0
j = len(array)-1
array.sort()
while i!= j :
    if array[i] + array[j] == x :
        result +=1
        i+=1
    elif array[i] + array[j] > x :
        j -=1
    else :
        i +=1
print(result)