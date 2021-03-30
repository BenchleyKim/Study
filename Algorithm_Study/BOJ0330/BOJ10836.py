import sys 
sys.stdin = open("./Algorithm_Study/BOJ0330/BOJ10836", "r")
input = sys.stdin.readline

M , N = map(int, input().split())
board = [[1]*M for _ in range(M)]
days = []
assumption_list = [0] * (2*M-1)
for _ in range(N) :  
  zero, one , two = map(int, input().split())
  for i in range(zero,one+zero) :
    assumption_list[i] += 1
  for i in range(one+zero, 2*M-1) :
    assumption_list[i] += 2

for i in range(M) :
  board[i][0] += assumption_list[M-1-i]
for i in range(1,M) :
  board[0][i] += assumption_list[M+i-1]

for i in range(1,M) :
  board[i][i] = max(board[i-1][i],board[i][i-1],board[i-1][i-1])
  for j in range(i+1,M) :
    board[j][i] = max(board[j-1][i],board[j][i-1],board[j-1][i-1])
    board[i][j] = max(board[i-1][j], board[i][j-1],board[i-1][j-1])
  
for line in board :
  for ele in line :
    print(ele, end=' ')
  print(end='\n')

# 0 1 2 
# 1 1 1
# 2 2 2 
# 3 4 5 

# 0 0 1 1 1 2 2
# 1 1 1 1 1 1 2
# 1 1 2 2 2 3 4