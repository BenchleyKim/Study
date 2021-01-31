n = 4 
m = 4
k = 2 
x = 1 
# roads = {}
# for _ in range(m):
#   a, b = list(map(int, input().split()))
#   if a in roads.keys()  :
#     roads[a] += [b]
#     continue
#   else :
#     roads[a] = [b] 

roads = {1: [2, 3], 2: [3, 4]}

checkList = {}
stack = []  
distances = {}

stack.append(x)
while True :
  if len(stack) == 0 :
    break
  root = stack.pop()
  if root in checkList.keys() : 
    continue
  checkList[root] = 1 
  print(root)
  if not root in roads.keys():
    continue
  sort = sorted(roads[root])
  print(sort)
  for s in sort :
    if s in checkList.keys():continue
    stack.append(s)