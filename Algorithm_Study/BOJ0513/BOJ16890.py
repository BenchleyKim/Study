import sys
from collections import deque
sys.stdin = open(".\Algorithm_Study\BOJ0513\BOJ16890","r")
input = sys.stdin.readline

A = list(input().rstrip())
B = list(input().rstrip())
N = len(A)

S = deque()
A = sorted(A,reverse=True)
B = sorted(B)
i = 0
hN = N // 2
if N % 2 :
    A = deque(A[hN:])
    B = deque(B[hN+1:])
else :
    A = deque(A[hN+1:])
    B = deque(B[hN+1:])



print(A)
print(B)
while i < N :
    if i % 2 :
        # 큐브 러버의 경우 
        if ord(A[-1]) < ord(B[-1]) :
            S.appendleft(B.pop())
        else :
            S.append(B.pop())
    else :
        if len(B) : 
            if ord(A[-1]) < ord(B[-1]) :
                S.appendleft(A.pop())
            else :
                S.append(A.pop())
        else :
            S.append()
    i += 1
print(S)
print("".join(S))


