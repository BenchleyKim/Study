import sys 
sys.stdin = open("./Algorithm_Study/BOJ0301/BOJ18870", "r")

# 수직선 위에 N개의 좌표 X1, X2, ..., XN이 있다. 이 좌표에 좌표 압축을 적용하려고 한다.

# Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표의 개수와 같아야 한다.

# X1, X2, ..., XN에 좌표 압축을 적용한 결과 X'1, X'2, ..., X'N를 출력해보자.

N = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))
check = [0]* N
arrSet = sorted(set(arr))
hash = {}
for i, a in enumerate(arrSet):
  hash[a] = i
for i in range(N) :
  print(hash[arr[i]], end=" ")
