a = int(input())
a = list(str(a))
count = [0]*10
for i in range(len(a)) :
    count[int(a[i])] += 1
if count.index(max(count)) == 9 or count.index(max(count)) == 6 :
    cnt = count[9] + count[6]
    if cnt %2 == 0 :
        count[9],count[6] = cnt//2,cnt//2
    else :
        count[9],count[6] = cnt//2+1,cnt//2+1
print(max(count))