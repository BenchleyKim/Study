import sys
sys.stdin = open("./Algorithm_Study/BOJ0319/BOJ10830", "r")
input = sys.stdin.readline
N,B = map(int, input().split())
Matrix = []
for _ in range(N) :
  Matrix.append(list(map(int,input().split())))
def MatrixMultply(A,B) :
  result = [[0] * N for _ in range(N)]
  for i in range(N) :
    for j in range(N) :
      s = 0
      for k in range(N) :
        s += A[i][k] * B[k][j]
      result[i][j] = s%1000
  return result
def devide(M, b) :
  if b == 1 :
    return M
  result = devide(MatrixMultply(M, M), b//2)
  if b % 2 == 0 :
    return result
  if b % 2 == 1 :
    return MatrixMultply(result, M)
for i in range(N) :
  for j in range(N) :
    if Matrix[i][j] >= 1000 :
      Matrix[i][j] = Matrix[i][j] % 1000
ans = devide(Matrix, B)
for i in range(N) :
  for j in range(N) :
    print(ans[i][j],end=' ')
  print(end='\n')

