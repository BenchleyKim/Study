import sys
import collections
sys.stdin = open("./Algorithm_Study/BOJ0325/BOJ14503", "r")
input = sys.stdin.readline
N , M = map(int, input().split())
R, C , D = map(int, input().split())
MAP = []
check = [[0]* M for _ in range(N)]
for _ in range(N) :
  MAP.append(list(map(int, input().split())))
dx = [1,-1,0,0]
dy = [0,0,1,-1]
direction = [[0,-1],[-1,0],[0,1],[1,0]]
def robot(R,C,D, action,count) :
  global cnt 
  if action == 1 : 
    if check[R][C] :
      pass
    else :
      check[R][C] = cnt
      cnt += 1
    count = 0
    robot(R,C,D,2,count)
    return
  if action == 2 :
    nx,ny = R+direction[D][0], C+direction[D][1]
    if count == 4:
      nr, nc = R - direction[(D+1)%4][0] , C - direction[(D+1)%4][1]
      if nr < 0 or nr >= N or nc < 0 or nc >= M :
        return
      if MAP[nr][nc] == 1 :
        return
      robot(nr,nc,D,1,count)
      return
    # 왼쪽 방향이 범위를 넘는지 넘으면 count ++
    if nx < 0 or nx >= N or ny < 0 or ny >= M :
      robot(R,C,(D+3)%4,2, count +1)
      return
    # 왼쪽방향이 이미 청소 되어 있거나 벽이라면 count++
    if check[nx][ny] or MAP[nx][ny]:
      robot(R,C,(D+3)%4,2, count +1)
      return
    # 왼쪽방향에 청소하지 않은 공간이 남아있다면 회전한 다음 그 칸으로 전진 
    robot(nx , ny , (D+3)%4 , 1 , count)
    return
cnt = 1
robot(R,C,D,1,0)
# for line in check:
#   print(line)
print(cnt-1)



    



  