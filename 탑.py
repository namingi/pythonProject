
n = int(input())
array= list(map(int, input().split()))
stack = []
stack.append((array[0],0))
print(0,end=" ")
for i in range(1,len(array)) :
   if stack[-1][0] > array[i] :
      print(stack[-1][1]+1,end=" ")
      stack.append((array[i],i))
   else :
      while stack[-1][0] < array[i] :
         stack.pop()
         if len(stack) == 0 :
            print(0,end=" ")
            break
      if len(stack) != 0 :
         print(stack[-1][1]+1,end=" ")
      stack.append((array[i],i))

