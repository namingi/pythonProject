from collections import deque
import sys
n = int(sys.stdin.readline())
queue = deque([i for i in range(1, n+1)])

while len(queue)>1 :
    queue.popleft()
    aa = queue.popleft()
    queue.append(aa)
    if len(queue) == 1 :
        break
print(queue[-1])