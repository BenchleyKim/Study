import sys 
sys.stdin = open("./Algorithm_Study/BOJ0329/BOJ5710", "r")
input = sys.stdin.readline
def calbill(K) :
  if K <= 100 :
    return 2*K
  if K <= 10000 :
    return (K-100)*3+200
  if K <= 1000000 :
    return (K-100-10000)*5+200+30000
  return (K-100-10000-1000000)*7+200+30000+5000000

def callwatt(K) :
  if K <= 200 :
    return K//2
  ans = 0
  if K > 200 :
    K -= 200
    ans += 100
  if K > 29700 :
    K -= 29700
    ans += 10000
  else :
    return ans + K//3
  if K > 4950000 :
    K -= 4950000
    ans += 1000000
  else :
    return ans+K//5
  return ans+K//7



print("callwatt")
print(callwatt(2900))

print(callwatt(35515))

print()
print(calbill(1000))
print(calbill(10223))

print(calbill(10223)-calbill(1000))


# def dac(left, right) :
#   mid = (left+right) //2
#   neighbor = total_watt - mid
#   diff = calbill(neighbor) - calbill(mid)
#   print(left, mid , right , diff)
#   if left == right :
#     print(calbill(right))
#     return
#   if diff < B :
#     dac(left+1, mid)
#   if diff > B :
#     dac(mid,right)


# while True :
#   A, B = map(int, input().split())
#   total_watt = 0
#   if A == 0 and B == 0 :
#     break
#   if A <= 200 :
#     total_watt = A//2
#   elif A <= 29900 :
#     total_watt = (A-200)//3+100
#   elif A <= 4979900 : 
#     total_watt = (A-29900)//5+10000+100
#   else :
#     total_watt = (A -4979900)//7+1000000+10000+100
#   print(total_watt) 
#   dac(0,total_watt)

  
