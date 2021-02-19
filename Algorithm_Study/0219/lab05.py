import sys 
sys.stdin = open("./Algorithm_Study/0219/lab05", "r")
N = int(input())
M = int(input())
n = [1] * N
arr = [0]*M
arr.extend(n)
pos = list(range(M,N+M))

# 세그먼트 트리로 구간합 계산하고 업데이트하는 방식으로 계산 MlogN의 복잡도 
for i in range(M) :
  dvd = int(input())
  idx = pos[dvd-1]
  arr[M-i-1] = 1
  arr[idx] = 0
  pos[dvd-1] = M-i-1
  print(arr)
  print(pos)
  
