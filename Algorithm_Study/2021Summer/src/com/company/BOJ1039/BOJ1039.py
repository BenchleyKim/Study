import sys
from itertools import combinations
from collections import deque
sys.stdin = open("./Algorithm_Study/2021Summer/src/com/company/BOJ1039/BOJ1039.in","r")
input = sys.stdin.readline

N, K = map(int,  input().split())
L = len(str(N))
if L <= 2 :
    if L < 2 :
        print(-1)
        exit()
    if str(N)[1] == '0' :
        print(-1)
        exit()
all_case = list(combinations(list(range(L)),2))
queue = deque()
queue.append(N)

while K > 0 :
    K -= 1
    c = set()
    mx = 0
    for i in range(len(queue)) :
        node = list(str(queue.popleft()))
        for i, j in all_case :
            node[i], node[j] = node[j] , node[i]
            if node[0] == '0' :
                node[i], node[j] = node[j] , node[i]
                continue
            sub = int("".join(node))
            node[i], node[j] = node[j] , node[i]
            if sub in c :
                continue
            mx = max(mx, sub)
            c.add(sub)
            queue.append(sub)

if mx :
    print(mx)
else :
    print(-1)


