import sys

sys.stdin = open('./Algorithm_study/0218/lab03','r')

N, M = map(int, input().split())

def gcd(m,n):
    while n != 0:
       t = m%n
       (m,n) = (n,t)
    return abs(m)
count = 0
for i in range(1,M+1): 
  if gcd(i,N) == 1 :
    count += 1

print(count)
