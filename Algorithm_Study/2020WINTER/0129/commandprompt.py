
n = int(input())
strList = []
for i in range(n):
  strList.append(input())
result = ""
len = len(strList[0])
i = 0
while i < len :
  r = strList[0][i]
  nextchar = r 
  for s in strList :
    if s[i] != r :
      nextchar = '?'
      break
  result += nextchar
  i += 1
print(result)
