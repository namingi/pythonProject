n = int(input())
array = list(map(int,input().split()))
temp = [0]*2
for i in range(len(array)) :
     M = array[i]//60
     Y = array[i]//30
     temp[0] += Y*10+10
     temp[1] += M*15+15
if temp[0] > temp[1] :
    print("M",end=" ")
    print(temp[1])
elif temp[0] < temp[1] :
    print("Y",end=" ")
    print(temp[0])
elif temp[0] == temp[1] :
    print("Y",end=" ")
    print("M",end=" ")
    print(temp[0])