import sys

sys.stdin = open("./Algorithm_Study/0217/boj2825", "r")


N = int(input())
arr = []
for _ in range(N) :
  arr.append(int(input()))
print(arr)

