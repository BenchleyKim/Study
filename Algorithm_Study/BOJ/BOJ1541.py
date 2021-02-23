import sys
sys.stdin = open("./Algorithm_Study/BOJ/BOJ1541", "r")
S = input()

R = []
num =  ""
flag = 0
cal  = []
for s in S:
  if s == '-' :
    R.append(int(num))
    cal.append(s)
    num =  ""
    continue
  if s == '+' :
    R.append(int(num))
    cal.append(s)
    num =  ""
    continue
  num = num + s
R.append(int(num))

result = R[0]
tmp = 0 
for i, c in enumerate(cal) :
  if flag == 1 :
    if c == '-' :
      result -= tmp
      tmp = R[i+1]
      continue
    if c == '+' :
      tmp += R[i+1]
  elif flag == 0 :
    if c == '-' :
      tmp = R[i+1]
      flag = 1
      continue
    if c == '+' :
      result += R[i+1]
if flag == 1 :
  result -= tmp
print(result)