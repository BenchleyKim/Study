import sys 
sys.stdin = open("./Algorithm_Study/BOJ/BOJ18870", "r")

N = int(input())
arr = list(map(int, input().split()))

def DAC(sub , rank) :
  tmp = sub.pop(0)
  left = []
  right = []
  mid = []
  for a in sub :
    if a == tmp :
      mid.append(a)
      continue
    if a > tmp :
      right.append(a)
      continue
    if a < tmp :
      left.append(a)
      continue
  rank = len(left)
  print(rank)
  DAC(left, rank)
  for m in mid : 
    print(rank)
  DAC(right,rank)



 



  