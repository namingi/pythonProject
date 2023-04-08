
T= 3
for _ in range(1,T+1) :
    array = list(map(int,input().split()))
    if array.count(1) == 0 :
        print("D")
    elif array.count(1) == 1 :
        print("C")
    elif array.count(1) == 2:
        print("B")
    elif array.count(1) == 3:
        print("A")
    elif array.count(1) == 4 :
        print("E")
