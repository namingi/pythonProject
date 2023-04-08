from collections import deque
import sys
n = int(sys.stdin.readline())
queue = deque()
def push(x) :
    queue.append(x)
def front() :
    if len(queue) == 0 :
        print(-1)
    else :
        print(queue[0])
def back() :
    if len(queue) == 0 :
        print(-1)
    else :
        print(queue[-1])
def empty() :
    if len(queue) == 0 :
        print(1)
    else :
        print(0)
def size() :
    print(len(queue))
def pop() :
    if len(queue) == 0 :
        print(-1)
    else :
        print(queue.popleft())


for _ in range(n) :
    array = list(map(str,sys.stdin.readline().split()))
    if array[0] == "push" :
        push(array[1])
    elif array[0] == "front" :
        front()
    elif array[0] == "size":
        size()
    elif array[0] == "back":
        back()
    elif array[0] == "empty" :
        empty()
    elif array[0] == "pop" :
        pop()
