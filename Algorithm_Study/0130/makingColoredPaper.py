# BOJ 2630

n = 8
paper = [] 
# for _ in range(n):
#   paper.append(list(map(int, input().split())))

pape = [[1, 1, 0, 0, 0, 0, 1, 1], [1, 1, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 0, 0, 0, 1, 1, 1, 1], [0, 1, 0, 0, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1, 
1]]


def isOne(paper,white,blue) :
  plen = len(paper)
  psum = sum([sum(p) for p in paper])
  if psum == 0 :
    white += 1 
    return True
  if psum == (plen ** 2) :
    blue += 1
    return True
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
    
  
# print(paperslice(pape))
white = 0
blue = 0 
queue = [pape]
while True :
  if len(queue) == 0 :
    print(white)
    print(blue)
    break
  temp = queue.pop(0)
  if isOne(temp,white,blue) : print(temp) ;continue
  Slices = paperslice(temp)
  for s in Slices:
    queue.append(s)



  
