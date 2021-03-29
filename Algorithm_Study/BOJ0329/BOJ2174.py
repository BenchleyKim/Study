import sys 
sys.stdin = open("./Algorithm_Study/BOJ0329/BOJ2174", "r")
input = sys.stdin.readline

A, B = map(int, input().split())
board = [[0] * A for _ in range(B) ]
N, M = map(int, input().split())
Robots = {}
dx = [-1,0,1,0]
dy = [0,1,0,-1]
points = {'N' : 0 , 'E' : 1, 'S':2, 'W':3}
for i in range(1,N+1) :
  X, Y, D = input().split()
  X, Y = int(X) , int(Y) 
  D = points[D]
  Robots[i] = [D, B-Y, X-1]
  board[B-Y][X-1] = i
Flag = True
for i in range(1,M+1) :
  rid, cmd, itr = input().split()
  rid , itr = int(rid), int(itr)
  cd, cx, cy = Robots[rid]
  if not Flag :
    break
  for i in range(itr) : 
    if cmd == 'L' :
      cd = (cd+3)%4
      Robots[rid][0] = cd
      continue
    if cmd =='R' :
      cd = (cd+1)%4
      Robots[rid][0] = cd
      continue
    if cmd == 'F' :
      nx, ny = cx+dx[cd], cy+dy[cd]
      if nx < 0 or nx >= B or ny < 0 or ny >= A :
        print("Robot {rid1} crashes into the wall".format(rid1=rid))
        Flag = False
        break
      if board[nx][ny] > 0 :
        print("Robot {rid1} crashes into robot {rid2}".format(rid1 = rid, rid2 = board[nx][ny]))
        Flag = False
        break
      board[nx][ny] = rid
      board[cx][cy] = 0
      Robots[rid] = [cd, nx, ny]
      cx, cy = nx,ny
if Flag :
  print("OK")



