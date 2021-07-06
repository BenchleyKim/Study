import sys
sys.stdin = open("./Algorithm_Study/2021Summer/src/com/SDS0706/BOJ7453/BOJ7453.in","r")
input = sys.stdin.readline

N = int(input())

A , B , C, D = [[0] * N for i in range(4)]
for i in range(N) :
    A[i], B[i] , C[i] ,D[i] = map(int, input().split())

print(A)
print(B)
print(C)
print(D)