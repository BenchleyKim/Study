
n = int(input())
table =[]
for _ in range(3):
  table.append(list(map(int, input().split())))

pattern = [(1,0,0),(0,1,0),(0,0,1),(1,0,1)]

def solve(idx, current, result) :
  if idx == n : return result
  if idx = 0 : 
  l = [current[0][idx-1],current[1][idx-1],current[2][idx-1]]
  temp = [table[0][idx],table[1][idx],table[2][idx]]
  idx += 1
  for p in pattern :
    if p & l != 0 : continue
    current = current.append(p * temp)
    currentSum = current.sum()
    solve(idx, current, currentSum )
  
solve(0,list())
  



  








