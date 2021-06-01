import sys 
import heapq
sys.stdin = open(".\Algorithm_Study\BOJ0427\BOJ1744","r")
input = sys.stdin.readline

N = int(input())
parr = []
narr = []
zarr = []

for i in range(N) :
    n = int(input())
    if n > 0 :
        parr.append(n)
    elif n < 0 :
        narr.append(n)
    else : 
        zarr.append(n)
parr.sort()
narr.sort(reverse=True)
ans = 0 
while len(narr) >= 2 :
    k1, k2 = narr.pop(), narr.pop()
    ans += k1*k2
while narr :
    if zarr :
        narr.pop()
        zarr.pop()
    else :
        ans += narr.pop()

while len(parr) >= 2:
    k1, k2 = parr.pop(), parr.pop()
    ans += max(k1 * k2, k1+k2)  
while parr : 
    ans += parr.pop()

print(ans)
        