import sys 
sys.stdin = open("./Algorithm_Study/0215/2231.txt", "r")
N = int(input())
def digitSum(n) :
  result = n 
  for k in str(n):
    result += int(k)
  return result
no = True
for i in range(N) :
  if digitSum(i) == N :
    print(i)
    no = False
    break
if no : 
  print(0)