import sys 
sys.stdin = open("./Algorithm_Study/BOJ/BOJ1620", "r")
N, M = map(int, input().split())
Dictonary = {}
for i in range(1,N+1) :
  name = input()
  Dictonary[name] = i
  Dictonary[i] = name
for _ in range(M):
  Q = input()
  if Q.isdecimal() :
    print(Dictonary[int(Q)])
  else :
    print(Dictonary[Q])