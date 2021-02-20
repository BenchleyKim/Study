import sys 
sys.stdin = open("./Algorithm_Study/BOJ/BOJ1697", "r")

N, K = map(int, input().split())
MAX = 100001
queue = [[N,0]]
checkList = [0] * MAX
while queue :
  tmp , count  = queue.pop(0)
  if tmp == K :
    print(count)
    exit()
  if 2*tmp > MAX :
    continue
  if (checkList[tmp] != 0) & (checkList[tmp] > count) :
    checkList[tmp] = count 
    continue
  checkList[tmp] = count
  queue.append([tmp-1,count+1]) 
  queue.append([tmp+1,count+1])
  queue.append([2*tmp,count+1])
