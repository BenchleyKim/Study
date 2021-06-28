
import sys
from random import * 

f = open("Algorithm_Study/STD0618/test04", 'w')
N , K = 10000, 100
f.write(f"1\n")
f.write(f"{N} {K}\n")
for i in range(N-1):
    arr = []
    for k in range(K) :
        arr.append("0")
    f.write("".join(arr) + "\n")
arr = []
for k in range(K) :
    arr.append("1")
f.write("".join(arr)+"\n")
f.close()