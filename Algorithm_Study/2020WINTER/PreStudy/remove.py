S = 'baabaa'
stack = []
for i in range(len(S)) :
  if stack :
    if S[i] == stack[-1] :
      stack.pop()
    else :
      stack.append(S[i])
  else : 
    stack.append(S[i])

if stack : 
  print(0)
else :
  print(1)