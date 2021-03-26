import sys
sys.stdin = open("./Algorithm_Study/BOJ0326/BOJ9252", "r")
input = sys.stdin.readline
str1 = input().rstrip()
str2 = input().rstrip()
DP = [[0] * (len(str2)+1 )for _ in range(len(str1)+1)]
for i in range(1,len(str1)+1) :
  for j in range(1,len(str2)+1) :
    if str1[i-1] == str2[j-1] :
      DP[i][j] = DP[i-1][j-1]+1
    else :
      DP[i][j] = max(DP[i][j-1], DP[i-1][j])

print(DP[len(str1)][len(str2)])
queue = [[len(str1),len(str2)]]
output = []
while queue :
  x,y = queue.pop(0)
  if DP[x][y] == 0 :
    break
  if DP[x-1][y] == DP[x][y] :
    queue.append([x-1,y]) 
  elif DP[x][y-1] == DP[x][y] :
    queue.append([x,y-1])
  elif DP[x-1][y-1] == DP[x][y] -1 :
    output.insert(0,str1[x-1])
    queue.append([x-1,y-1])
for out in output :
  print(out, end='')