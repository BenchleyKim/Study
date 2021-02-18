import sys
sys.stdin = open('./Algorithm_study/0218/lab04test','r')

N, K = map(int, input().split())
stones = list(map(int,input().split()))
mn = K
for i in range(N-K+1) : 
  k = K
  tmp = max(stones[i:i+K])
  mn = min(mn,tmp )
print(mn)

