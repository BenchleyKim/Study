import sys 
sys.stdin = open("./Algorithm_Study/BOJ/BOJ7662", "r")

T = int(sys.stdin.readline())
for _ in range(T) :
  Q = []
  K = int(sys.stdin.readline())
  for _ in range(K) :
    C, N = sys.stdin.readline().split()
    N = int(N)
    if C == 'I' :
      Q.append(N)
      continue
    if C == 'D' :
      if len(Q) == 0 :
        continue
      if N == 1 :
        # 최대값 삭제
        continue
      if N == -1 :
        # 최소값 삭제
        continue
  if len(Q) == 0 :
    print('EMPTY')
  else :
    # 최대값 , 최소값 출력 
    print()
    
