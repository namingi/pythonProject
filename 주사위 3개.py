n,m,k = map(int,input().split())
if n==m==k :
    print(10000+n*1000)
elif n !=m and m !=k and k !=n :
    print(max(n,m,k)*100)
elif (n==m and m!=k) :
    print(1000+n*100)
elif (n==k and m!=k) :
    print(1000+n*100)
elif (m==k and n!=m) :
    print(1000+m*100)
