import sys
sys.stdin = open("./Algorithm_Study/BOJ0317/BOJ2166", "r")

N = int(sys.stdin.readline())
points = []
for _ in range(N):
  points.append(list(map(int, sys.stdin.readline().split())))
points.append(points[0])
xs = 0
for i in range(N) :
  xs += points[i][0] * points[i+1][1]
  xs -= points[i][1] * points[i+1][0]
print(abs(xs) / 2)
  
      