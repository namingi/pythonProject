array = [i for i in range(21)]
for _ in range(10) :
    a,b= map(int,input().split())
    cnt = (b-a+1)//2
    for i in range(cnt) :
        array[a+i],array[b-i] = array[b-i],array[a+i]
array.pop(0)
for j in range(len(array)) :
    print(array[j],end=" ")