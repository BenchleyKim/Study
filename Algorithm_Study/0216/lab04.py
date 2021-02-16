import sys 
sys.stdin = open("./Algorithm_Study/0216/lab04", "r")

N , M = map(int, input().split())
T = list(map(int, input().split()))
result = 0
def binarySearch(left, right) :
  global result
  print(left, right)
  if left == right :
    result = left
    return
  mid = (left + right) // 2
  m = 0
  for t in T :
    m += mid // t
  if m < M : binarySearch(mid+1,right)
  else : binarySearch(left, mid)
mt = min(T) * M
binarySearch(0,mt)
print(result) 
