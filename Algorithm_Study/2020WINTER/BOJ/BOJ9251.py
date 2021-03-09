import sys 
sys.stdin = open("./Algorithm_Study/BOJ/BOJ9251", "r")

STR1 = input()
STR2 = input()

arr = [[0] * (len(STR2)+1) for _ in range(len(STR1)+1)]

mx = 0
for i in range(1, len(STR1)+1) :
  for j in range(1,len(STR2)+1) :
    if STR1[i-1] == STR2[j-1] :
      arr[i][j] = arr[i-1][j-1] + 1
      mx = max(mx, arr[i][j])
    else :
      if arr[i-1][j] < arr[i][j-1] :
        arr[i][j] = arr[i][j-1] 
        continue
      arr[i][j] = arr[i-1][j]
print(mx)
