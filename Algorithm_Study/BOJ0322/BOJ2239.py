import sys
sys.stdin = open("./Algorithm_Study/BOJ0322/BOJ2239", "r")
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
table = []
for _ in range(9) :
  line = list(map(int, list(input().rstrip())))
  table.append(line)
  print(line)

def backtracking(board) :
  # for b in board :
  #   print(b)
  checkcol = {i:[] for i in range(9)}
  checkrow = {i:[] for i in range(9)}
  checkblock = {i:[] for i in range(9)}
  searchList = []
  flag = 0
  for i in range(3) :
    for j in range(3) :
      for r in range(3) :
        for l in range(3) :
          x, y, b = 3*i+r, 3*j+l, 3*i + j
          if board[x][y] == 0 :
            searchList.append([x,y,b])
            flag = 1
            continue
          checkcol[x].append(board[x][y])
          checkrow[y].append(board[x][y])
          checkblock[b].append(board[x][y])
  if not flag :
    for i in range(9) :
      for j in range(9) :
        print(board[i][j],end="")
      print()
    print()
  # print(searchList)
  # print(checkcol)
  # print(checkrow)
  # print(checkblock)
  for s in searchList :
    x,y,b = s
    for i in range(1,10) :
      if (i in checkcol[x]) or (i in checkrow[y]) or (i in checkblock[b]) :
        continue
      board[x][y] = i
      print(x,y,i)
      backtracking(board)


backtracking(table)