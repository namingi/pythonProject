array = []
sum = 0
for _ in range(5) :
    a = int(input())
    array.append(a)
    sum += a
print(int(sum/5))
array.sort()
print(array[2])