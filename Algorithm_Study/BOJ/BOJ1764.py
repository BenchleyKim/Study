import sys 
sys.stdin = open("./Algorithm_Study/BOJ/BOJ1764", "r")

N, M = map(int, input().split())
A = {}
for i in range(N) :
  S = input()
  A[S] = 1 
B = {}
for j in range(M) :
  S = input()
  if S in A.keys() :
    

