import sys
import heapq
sys.stdin = open("./Algorithm_Study/2021Summer/src/com/SDS0706/BOJ2143/BOJ2143.in","r")
input = sys.stdin.readline

T = int(input())
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

sumA = [A[0]]
for i in range(1,N) :
    sumA.append(A[i] + sumA[i-1])

sumB = [B[0]]
for i in range(1,M) :
    sumB.append(B[i] + sumB[i-1])
A_dict = {}
for i in range(N) :
    if sumA[i] in A_dict :
        A_dict[sumA[i]] += 1
    else :
        A_dict[sumA[i]] = 1
    for j in range(i+1, N) :
        k = sumA[j] - sumA[i] 
        if k in A_dict :
            A_dict[k] += 1
        else :
            A_dict[k] = 1
B_dict = {}
for i in range(M) :
    if sumB[i] in B_dict :
        B_dict[sumB[i]] += 1
    else :
        B_dict[sumB[i]] = 1
    for j in range(i+1, M) :
        k = sumB[j] - sumB[i] 
        if k in B_dict :
            B_dict[k] += 1
        else :
            B_dict[k] = 1    
answer = 0 
for A_key in A_dict.keys() :
    A_left = A_dict[A_key]
    B_key = T - A_key
    if B_key in B_dict :
        answer += A_left * B_dict[B_key]
print(answer)
