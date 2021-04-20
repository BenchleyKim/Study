import sys 
sys.stdin = open("./Algorithm_Study/BOJ0329/BOJ5710", "r")
input = sys.stdin.readline
def calbill(K) :
  if K <= 100 :
    return 2*K
  if K <= 10000 :
    return (K-100)*3+200
  if K <= 1000000 :
    return (K-10000)*5+29900
  return (K-1000000)*7+4979900

def callwatt(K) :
  if K <= 200 :
    return K//2
  ans = 0
  if K > 200 :
    K -= 200
    ans += 100
  if K > 29700 :
    K -= 29700
    ans += 9900
  else :
    return ans + K//3
  if K > 4950000 :
    K -= 4950000
    ans += 990000
  else :
    return ans+K//5
  return ans+K//7


def dac(left, right) :
  mid = (left+right) //2
  neighbor = total_watt - mid
  diff = calbill(neighbor) - calbill(mid)
  if diff == B :
    print(calbill(mid))
    return
  if diff < B :
    dac(left, mid-1)
  if diff > B :
    dac(mid+1,right)


while True :
  A, B = map(int, input().split())
  
  if A == 0 and B == 0 :
    break
  total_watt = callwatt(A)
  dac(0,total_watt)

  
