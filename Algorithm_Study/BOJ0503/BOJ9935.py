import sys
from collections import deque

sys.stdin = open(".\Algorithm_Study\BOJ0503\BOJ9935","r")
input = sys.stdin.readline

S = list(input().rstrip())
bomb = list(input().rstrip())

temp = deque()

for s in S:
    temp.append(s)

    if len(temp) >= len(bomb):
        check = True

        for i in range(len(bomb)):
            if temp[len(temp)-len(bomb)+i] != bomb[i]:
                check = False

        if check == True:
            for _ in range(len(bomb)):
                temp.pop()
if temp:
    print(("").join(temp))
else:
    print("FRULA")
