w = str(input())
w = w.upper()
cset = {}
for c in w:
  if c in cset.keys():
    cset[c] += 1
    continue
  cset[c] = 0
result = w[0]
max = 0
for i in cset.keys():
  if cset[i] > max :
    max = cset[i]
    result = i

if list(cset.values()).count(max) > 1 :
  print("?")
else :
  print(result)
