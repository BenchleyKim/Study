x = input()

def digitsum(x) :
  result = 0 
  for i in x :
    result += int(i)
  return str(result)

count = 0 
while len(x) > 1 :
  x = digitsum(x)
  count  += 1
print(count)
if int(x) in [3,6,9] :
  print("YES")
else :
  print("NO")