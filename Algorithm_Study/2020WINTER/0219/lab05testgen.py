import sys 
import random
sys.stdout = open("./Algorithm_Study/0219/lab05test", "w")

N = random.randrange(20000,100000)
M = random.randrange(20000,100000)
print(N)
print(M)
for _ in range(M) :
  a = random.randrange(1,N)
  print(a) 
