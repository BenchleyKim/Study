import sys 
import collections
sys.stdin = open("./Algorithm_Study/BOJ/BOJ1697", "r")

N, K = map(int, input().split())
MAX = 100001
arr = [MAX] * MAX 
arr[K] = 1
check = [0] * MAX
queue = collections.deque([(N,0)])

while queue :
  tmp,count = queue.popleft()
  if tmp < 0 or tmp >= MAX :
    continue
  if tmp == K :
    print(count)
    break
  if check[tmp] == 1 :
    continue
  check[tmp] = 1
  queue.extend([(tmp-1,count+1),(tmp+1,count+1),(tmp*2,count+1)])


