import sys
sys.stdin = open('./Algorithm_study/0217/lab02','r')
N= int(input())
arr = [0 ] * (N+1)
arr[1] = 1
arr[2] = 2
for i in range(3,N+1) :
  s = 2
  for j in range(1,i-1) :
    s += arr[j]
  arr[i] = s
  
print(arr)
# print(N)