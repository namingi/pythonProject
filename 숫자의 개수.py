a = int(input())
b = int(input())
c = int(input())

value = list(str(a*b*c))
count = [0]*10
for i in range(len(value)) :
    count[int(value[i])]+=1
for j in range(len(count)) :
    print(count[j], end=" ")
