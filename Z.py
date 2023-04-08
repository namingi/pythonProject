n, r, c = map(int, input().split())

def func(n,r,c) :
    if n == 0 :
        return 0
    size = 2**(n-1)
    if r<size and c<size :
        return func(n-1,r,c)
    if r<size and c<=size :
        return size*size + func(n-1,r,c-size)
    if r>=size and c<size :
        return 2*size*size + func(n-1,r-size,c)
    if r>=size and c>= size :
        return 3*size*size + func(n-1,r-size,c-size)

print(func(n,r,c))
