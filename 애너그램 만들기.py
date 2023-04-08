a = [0]*26
b = [0]*26
A = list(input())
B = list(input())
result = 0
for i in A :
    a[ord(i)-97] += 1
for i in B :
    b[ord(i)-97] += 1
for i in range(26) :
    result += abs(a[i]-b[i])
print(result)