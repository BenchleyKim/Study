import sys 
sys.stdin = open("./Algorithm_Study/0219/lab05", "r")
N = int(input())
M = int(input())
n = list(range(1,N+1))
arr = [0]*M
arr.extend(n)
print(arr)
pos = list(range(M,N+M))
print(pos)


for i in range(M) :
  dvd = int(input())
  idx = pos[dvd-1]
  arr[M-i-1] = arr[idx]
  arr[idx] = 0
  pos[dvd-1] = M-i-1
  print(arr)
  print(pos)
  
