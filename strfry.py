T = int(input())

for _ in range(T) :
    x,y = map(str,input().split())
    string = "Possible"
    x = sorted(x)
    y = sorted(y)
    if x != y :
        string = "Impossible"
    print(string)