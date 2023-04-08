import sys
input = sys.stdin.readline
T = int(input())
for _ in range(1,T+1) :
    a,b = map(int, input().split())
    print(a+b)