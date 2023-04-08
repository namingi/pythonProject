
a,b,c = map(int,input().split())
def multiple(a,b) :
    if b == 1 :
        return a%c
    else :
        tmp = multiple(a,b//2)
        if b %2 == 0 :
            return tmp*tmp%c
        else :
            return tmp*tmp*a%c
print(multiple(a,b))
