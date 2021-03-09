n, s = input().split()
n = int(n)
log = [ ]
correct = None
for i in range(n):
  name, answer = input().split()
  if name == s :
    correct = answer
  else : 
    if not correct :
      log.append(answer)

print(log.count(correct))