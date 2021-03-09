import sys
sys.stdin = open('./Algorithm_study/0218/boj1107','r')

N = input()
M = int(input())
broken = list(map(int, input().split()))
l = len(N)
result = 0
if M == 10 :
  print(abs(int(N)-100))
  exit()
if int(N) == 100 :
  print(0)
  exit()
for n in N :
  l -= 1
  n = int(n)
  buttonList = range(0,9)
  # print(result)
  result += 1
  if n in broken :
    mn = 9
    for button in buttonList :
      if button in broken :
        continue
      else :
        mn = min(mn, abs(n-button))
    result += mn*(10**l)
    
print(result)
