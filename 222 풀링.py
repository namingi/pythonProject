n = int(input())
array = []
for _ in range(n) :
    array.append(list(map(int,input().split())))

def recursive(n,x,y):
    if n == 2 :
        tmp = []
        tmp.append(array[x][y])
        tmp.append(array[x][y+1])
        tmp.append(array[x+1][y])
        tmp.append(array[x+1][y+1])
        tmp.sort()
        return tmp[-2]
    else :
        first = recursive(n//2,x,y)
        second = recursive(n//2,x+n//2,y)
        third = recursive(n//2,x,y+n//2)
        fourth = recursive(n//2,x+n//2,y+n//2)
        tmp_2 = [first,second,third,fourth]
        tmp_2.sort()
        return tmp_2[-2]



print(recursive(n,0,0))