import sys 
sys.stdin = open("./Algorithm_Study/0215/4153.txt", "r")
a, b, c= sorted(list(map(int, input().split())))
while not (a == 0 and b== 0 and c == 0) : 
  if c**2 == b**2 + a ** 2 :
    print("right")
  else : 
    print("wrong")
  a , b, c = sorted(list(map(int, input().split())))