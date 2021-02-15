import sys 
sys.stdin = open("./Algorithm_Study/0215/lab01", "r")
n = int(input())
l = list(map(int,input().split()))
count = 0
for i in range(n) :
  if i == 0 :
    continue
  if l[i-1] < l[i] :
    # print(l[i])
    count += 1

print(count)

  
