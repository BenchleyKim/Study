import sys 
sys.stdin = open("./Algorithm_Study/BOJ0402/BOJ17387", "r")
input = sys.stdin.readline
x1,y1,x2,y2 = map(int, input().split())
x3,y3,x4,y4 = map(int, input().split())

A = (x1,y1)
B = (x2,y2)
C = (x3,y3)
D = (x4,y4)

def ccw(a,b,c) :
  s = (b[0] - a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])
  # 반시계 방향
  if s > 0 : return 1
  # 시계방향 
  if s  < 0 : return -1
  # 평행 
  if s==0 : return 0

check_first = ccw(A,B,C) * ccw(A,B,D) 
check_second = ccw(C,D,A) * ccw(C,D,B)
if check_first == 0 and check_second == 0 :
  if A > B :
    A, B = B, A 
  if C > D :
    C, D = D, A
  if C<=B and A<=D :
    print(1)
  else :
    print(0)
  sys.exit()

if check_first <= 0  and check_second <= 0 :
  print(1)
else :
  print(0)