import sys
import random
sys.stdout = open("./Algorithm_Study/0219/lab03test", "w")

N = random.randrange(400,1000)
print(N)
for _ in range(N):
  print(random.randrange(1,1000000),end = ' ')
M = random.randrange(400,1000)
print()
print(M)
for _ in range(M):
  print(random.randrange(1,1000000),end = ' ')