import sys 
sys.stdin = open("./Algorithm_Study/BOJ0330/BOJ10836", "r")
input = sys.stdin.readline

M , N = map(int, input().split())
ans_board = [[1]*M for _ in range(M)]
days = []
for _ in range(N) :
  board = [[0]*M for _ in range(M)]
  first_growth = list(map(int, input().split()))
  cnt = 0
  for i in range(3) :
    for j in range(first_growth[i]) :
      cnt += 1
      if cnt > M :
        board[0][cnt-M] += i
        continue
      board[M-cnt][0] += i
  for i in range(M-1,0,-1) :
    itr = 2*i -1 
    for j in range(itr) :
      if j >= i :
        # 오른쪽으로 
        board[M-i][M-i+j-i+1] = max(board[M-i-1][M-i+j-i+1],board[M-i][M-i+j-i-1+1],board[M-i-1][M-i+j-i-1+1])
        continue
      board[M-i+j][M-i] = max(board[M-i+j-1][M-i], board[M-i+j][M-i-1], board[M-i+j-1][M-i-1])
# i = 3 일 때 board[1+j][1] += (j는 0~4)
# i = 2 일 때 board[2+j][2] += (j는 0~2)
  # print(" 증가 값 보드")
  # for b in board :
  #   print(b)
  
  for i in range(M) :
    for j in range(M) :
      ans_board[i][j] += board[i][j]
for line in ans_board :
  for ele in line :
    print(ele, end=' ')
  print(end='\n')

