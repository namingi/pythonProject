a,b= map(int,input().split())
cnt = max(a,b)-min(a,b)-1
print(cnt)
for i in range(min(a,b)+1,max(a,b)) :
    print(i,end=" ")