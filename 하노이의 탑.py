n = int(input())
def func(a,b,n) :
    if n == 1 :
        return print(a,b)
    else :
        func(a,6-a-b,n-1)
        print(a,b)
        func(6-a-b,b,n-1)
print(2**n-1)
func(1,3,n)