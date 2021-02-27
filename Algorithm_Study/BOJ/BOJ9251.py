import sys 
sys.stdin = open("./Algorithm_Study/BOJ/BOJ9251", "r")

STR1 = input()
STR2 = input()

arr = [[0] * len(STR1) for _ in range(len(STR2))]
mx = 0
for i in range(len(STR1)) :
  for j in range(len(STR2)) :
    if i == 0 :
      if STR1[i] == STR2[j] :
        arr[j:][i] =  1
        break
    else :
      if STR1[i] == STR2[j] :
        for k in range(j,len(STR2)) :
          arr[k][i] = arr[k][i-1] + 1
        break
      arr[j][i] = arr[j][i-1]
    

mx = 0 
print(max(arr[-1]))
