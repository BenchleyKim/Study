import sys
from collections import deque 
sys.stdin = open("./Algorithm_Study/2021Summer/src/com/SDS0706/BOJ11003/BOJ11003.in","r")
input = sys.stdin.readline

N, L = map(int, input().split())
arr = list(map(int, input().split()))
D = ["null"] * N 
dq = deque()
for i in range(N) :
    while dq and dq[-1][0] > arr[i] :
        dq.pop()
    while dq and i - dq[0][1] >= L :
        dq.popleft() 
    dq.append((arr[i], i))
    D[i] = dq[0][0] 
print(*D)