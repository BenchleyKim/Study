import sys 
sys.stdin = open("./Algorithm_Study/0215/1012.txt", "r")
for _ in range(int(input())) :
  M , N , K = map(int, input().split())
  m = [[0]*(M+2) for _ in range(N+2)]
  # print(m)
  checkList = []
  for _ in range(K) : 
    x,y  = list(map(int,input().split()))
    m[y+1][x+1] = 1
    checkList.append([y+1,x+1])
  for a in m :
    print(a)
  for a in checkList :
    dfs(a)
  print(checkList)
    
def dfs(pos) :
  if m[pos[0]][pos[1]] == 2 : 
    return 
  m[pos[0]][pos[1]] += 1
  if m[pos[0]+1][pos[1]] == 1 :
    dfs([pos[0]+1,pos[1]])
    m[pos[0]]

  m[pos[0]][pos[1]] 
  


