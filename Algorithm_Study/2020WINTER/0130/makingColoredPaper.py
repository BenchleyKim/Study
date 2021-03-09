# BOJ 2630

n = int(input())
pape = [] 
for _ in range(n):
  pape.append(list(map(int, input().split())))
white = 0
blue = 0   

def isOne(paper) :
  global white
  global blue  
  plen = len(paper)
  psum = sum([sum(p) for p in paper])
  if psum == 0 :
    white = white+1 
    return white
  if psum == (plen ** 2) :
    
    blue = blue+1
    return blue
  else :
    return False

def paperslice(paper) :
  l = int(len(paper)/2)
  p1 = []
  p2 = []
  p3 = []
  p4 = []
  for i,p in enumerate(paper) :
    if i >= l :
      p3.append(p[:l])
      p4.append(p[l:])
      continue
    else :
      p1.append(p[:l])
      p2.append(p[l:])
  return [p1,p2,p3,p4]

queue = [pape]
while True :
  if len(queue) == 0 :
    print(white)
    print(blue)
    break
  temp = queue.pop(0)
  if isOne(temp) : continue
  Slices = paperslice(temp)
  for s in Slices:
    queue.append(s)


  
