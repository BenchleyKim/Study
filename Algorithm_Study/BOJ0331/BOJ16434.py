import sys 
import math
sys.stdin = open("./Algorithm_Study/BOJ0331/BOJ16434", "r")
input = sys.stdin.readline

N, Hatk = map(int, input().split())
dungeon =[]
for _ in range(N):
  dungeon.append(list(map(int,input().split())))
mx = 0
mn = sys.maxsize
for room in dungeon :
  t,a,h = room
  if t == 1 :
    mx = max(mx, a*h)
    mn = min(mn, a*h)

def binsearch(left,right) :
  if left >= right :
    print(left)
    return
  Hmaxhp = (left + right)//2 
  Hcuratk = Hatk
  Hcurhp = Hmaxhp
  isClear = True
  for i in range(N) :
    T, A, H = dungeon[i]
    if T == 1 :
      # 때릴 수 있는 횟수
      if H % Hcuratk == 0 :
        Hcurhp -= ((H//Hcuratk-1)*A)
      else :
        Hcurhp -= ((H//Hcuratk)*A)
      atkcount = math.ceil(H/Hcuratk)
      # 맞을 수 있는 횟수 
    if Hcurhp <= 0 :
      isClear = False
      break
    if T == 2 :
      Hcuratk += A 
      Hcurhp = min(Hmaxhp, Hcurhp+H)
  if isClear : 
    binsearch(left, Hmaxhp-1)
  else :
    binsearch(Hmaxhp+1,right)
  return
    
binsearch(1,mx)

