import sys
sys.stdin = open("./Algorithm_Study/BOJ/BOJ11399", "r")

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
R = 0
S = 0 
for i in arr :
  S += i
  R += S
print(R)
