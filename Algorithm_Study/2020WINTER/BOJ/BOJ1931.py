import sys
sys.stdin = open("./Algorithm_Study/BOJ/BOJ1931", "r")

N = int(sys.stdin.readline())
arr = []
for _ in range(N) :
  arr.append(tuple(map(int,sys.stdin.readline().split())))
arr.sort()
prev = arr.pop(0)
count = 1
for a in arr :
  if a[0] >= prev[1] :
    count += 1
    prev = a
    continue
  if a[1] <= prev[1] : 
    prev = a
    continue


print(count)