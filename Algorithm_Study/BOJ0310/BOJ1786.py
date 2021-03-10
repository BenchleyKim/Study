import sys 
sys.stdin = open("./Algorithm_Study/BOJ0310/BOJ1786", "r")

T = sys.stdin.readline().rstrip()
P = sys.stdin.readline().rstrip()
print(P)
print(len(P))
pl = len(P)
tl = len(T)
F = [0] * pl 
for i in range(pl) :
  j = i-1
  while j >= 0 :
    print(P[:j], P[i-j:i])
    if P[:j] == P[i-j:i] :
      F[i] = j
      break
    j -= 1
  print(F)
  
