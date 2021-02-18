import sys
sys.stdin = open('./Algorithm_study/0218/lab04','r')

N, K = map(int, input().split())
stones = list(map(int,input().split()))
print(stones)
count = 0 
while True :
  count += 1
  k = K
  for i in range(N) : 
    if k == 0 :
      break
    if stones[i] == 0 :
      k -= 1
      continue
    stones[i] -= 1
  if k == 0 :
    print(count)
    break

