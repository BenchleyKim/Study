import sys 
sys.stdin = open("./Algorithm_Study/0215/15829", "r")
L = int(input())
S = input()
r= 31
M = 1234567891
result = 0
for e, s in enumerate(S) :
  i = ord(s)-96%M
  b =r**e %M
  result += (i*b)
print(result)
  