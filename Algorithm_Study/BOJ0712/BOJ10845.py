import sys
from collections import deque
sys.stdin = open("./Algorithm_Study/BOJ0712/BOJ10845.in","r")
input = sys.stdin.readline

N =  int(input())
queue = deque()
for i in range(N) :
    cmd = input().rstrip()
    if cmd.startswith("push") :
        c, v = cmd.split()
        queue.append(v)
        continue
    if cmd.startswith("front") :
        if queue :
            print(queue[0])
        else :
            print(-1)
        continue
    if cmd.startswith("size") :
        print(len(queue))
        continue
    if cmd.startswith("pop") :
        if queue :
            print(queue.popleft())
        else :
            print(-1)
        continue
    if cmd.startswith("empty") :
        if queue:
            print(0)
        else :
            print(1)

        continue
    if cmd.startswith("back") :
        if queue:
            print(queue[-1])
        else :
            print(-1)
        continue
