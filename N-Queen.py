import sys
n = int(sys.stdin.readline())
result = 0
visited_1 = [0]*n
visited_2 = [0]*(2*n-1)
visited_3  = [0] *(2*n-1)
def recur(x) :
    global result
    if x == n :
        result += 1
        return
    else :
        for j in range(n) :
            if not visited_1[j] and not visited_2[x-j+n-1] and not visited_3[x+j] :
                visited_1[j] = 1
                visited_2[x-j+n-1] = 1
                visited_3[x+j] = 1
                recur(x+1)
                visited_1[j] = 0
                visited_2[x-j+n-1] = 0
                visited_3[x+j] = 0
recur(0)
print(result)