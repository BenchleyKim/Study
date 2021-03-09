# N = 7

N = int(input())
sum = 1
count = 1
for i in range(0,N+1,6):
  sum += i
  # print("sum : " + str(sum))
  if sum >= N :
    break
  count += 1
print(count)
    
    
  