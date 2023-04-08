array = []
for i in range(9) :
    array.append(int(input()))
max_value = max(array)
for i in range(len(array)) :
    if array[i] == max_value:
        value = i
print(max_value)
print(value+1)