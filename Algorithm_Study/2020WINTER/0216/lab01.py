import sys 
sys.stdin = open("./Algorithm_Study/0216/lab01", "r")

S = input()
m = len(S)
mi = len(S)
for i in range(len(S)-1, len(S)//2-1,-1) : 
  # print(S[i], S[i:])
  l = i
  for j in range(len(S[i:])) :
    print(i,j,S[i-j],S[i+j],l)
    if S[i-j]==S[i+j] :
      l -= 1
      # print(l)
    else : 
      l = i
      break
  if m > l :
    m = l 
    mi = i
def makePelin(S,i) :
  rs = S[:i-1:-1]
  result = S[:i+1] + rs
  if i % 2 == 0:
    result += S[0]
  return result
  
  # print(S[:i])
  # rs = S[:i:-1]
  # result = S[:i]+ rs
  # return result
print(makePelin(S,mi))
print(m,mi)

