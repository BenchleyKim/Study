import sys 
sys.stdin = open("./Algorithm_Study/0219/lab04", "r")
S = input()
calPrior = {'(' : 1, ')':1, '*':3, '/':3, '+':2, '-':2}
num = []
stack  = []
newS = ''
for i in range(len(S)) :
  if S[i] == '(' :
    stack.append(S[i])
    continue
  if S[i] == ')':
    while stack[-1] != '(' :
      newS += stack.pop()
    stack.pop()
    continue
  if S[i] not in '()+-*/':
    newS += S[i]
    continue
  if len(stack) and calPrior[S[i]] <= calPrior[stack[-1]] :
    newS += stack.pop()
    stack.append(S[i])
    continue
  else :
    stack.append(S[i])
while len(stack) != 0 :
  newS += stack.pop()
print(newS)

    