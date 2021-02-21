import sys 
sys.stdin = open("./Algorithm_Study/BOJ/BOJ1012", "r")

T = int(input())
for _ in range(T) :
  M, N, K = map(int, input().split())
  B = [[0] * (N+1) for _ in range(M+1)]
  for _ in range(K) :
    X, Y= map(int,input().split())
    B[X][Y] = 1
  for i in B :
    print(i)


