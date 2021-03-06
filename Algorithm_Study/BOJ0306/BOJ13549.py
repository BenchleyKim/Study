import sys 
from collections import deque
sys.stdin = open("./Algorithm_Study/BOJ0306/BOJ13549", "r")
MAX = 100000
N, K = map(int, sys.stdin.readline().split())

queue = deque([(N,0)])
check = [0] * MAX * 2
while queue :
  tmp , count = queue.popleft()
  if tmp == K : 
    print(count)
    break
  if tmp >= 2*MAX or tmp <= 0 : 
    continue
  if check[tmp] == 1 :
    continue
  check[tmp] = 1
  queue.append((2*tmp,count))
  queue.append((tmp-1,count+1))
  queue.append((tmp+1,count+1))
  
