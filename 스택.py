import sys
array = []
n = int(sys.stdin.readline())
def push(x) :
    array.append(x)
def top() :
    if len(array) == 0 :
        print(-1)
    else :
        print(array[-1])
def size() :
    print(len(array))
def pop() :
    if len(array) == 0 :
        print(-1)
    else :
        print(array.pop())
def empty() :
    if len(array) == 0 :
        print(1)
    else :
        print(0)
for _ in range(n) :
    a = list(map(str,sys.stdin.readline().split()))
    if a[0]=="push" :
        push(int(a[-1]))
    elif a[0]=="top" :
        top()
    elif a[0] == "empty" :
        empty()
    elif a[0] == "size":
        size()
    elif a[0] == "pop":
        pop()