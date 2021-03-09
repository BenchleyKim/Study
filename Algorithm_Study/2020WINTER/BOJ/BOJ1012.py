import sys 
sys.stdin = open("./Algorithm_Study/BOJ/BOJ1012", "r")
dx = [0,0,1,-1]
dy = [1,-1,0,0]
T = int(input())
for _ in range(T) :
  M, N, K = map(int, input().split())
  B = [[0] * (N+1) for _ in range(M+1)]
  stack = []
  for _ in range(K) :
    X, Y= map(int,input().split())
    B[X][Y] = 1
  count = 0
  stack = []
  checkList = [[0] * (N+1) for _ in range(M+1)]
  for k in range(M):
    for j in range(N) :
      if (B[k][j] == 1) & (checkList[k][j] == 0):
        count += 1
        stack.append((k,j))
        while stack :
          tmp = stack.pop()
          if checkList[tmp[0]][tmp[1]] == 1 :
            continue
          checkList[tmp[0]][tmp[1]] = 1
          for i in range(4) :
            if (dy[i]+tmp[1] <= N) & (dy[i]+tmp[1] >= 0) & (dx[i]+tmp[0] <= M) & (dx[i]+tmp[0] >= 0) & (B[dx[i]+tmp[0]][dy[i]+tmp[1]] == 1 ) :
              stack.append((dx[i]+tmp[0],dy[i]+tmp[1]))
  
  print(count)




  # for i in B :
  #   print(i)



