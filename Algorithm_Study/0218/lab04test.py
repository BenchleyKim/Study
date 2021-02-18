import random
import sys
sys.stdout = open('./Algorithm_study/0218/lab04test','w')


N = random.randrange(40000,100000)
K = random.randrange(1,N)
print(N, end = " ")
print(K)
for _ in range(N):
  a = random.randrange(100,100000)
  print(a,end = " ")
