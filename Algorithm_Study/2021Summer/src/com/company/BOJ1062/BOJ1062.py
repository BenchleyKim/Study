import sys
from itertools import combinations
sys.stdin = open("./Algorithm_Study/2021Summer/src/com/company/BOJ1062/BOJ1062.in","r")
input = sys.stdin.readline

N , K = map(int, input().split())
if K < 5 :
    print(0)
    exit()
base = {'a', 'n', 't', 'i', 'c'}
other = set("bdefghjklmopqrsuvwxyz")
all_case = list(combinations(other, K-5))
answer = 0
words = [input().rstrip() for _ in range(N)]
mx = 0 
for case in all_case :
    case = base | set(case)
    cnt = 0 
    for word in words :
        flag = True
        for w in word :
            if not w in case :
                flag = False
                break
        if flag : 
            cnt += 1
    mx = max(mx, cnt)
print(mx)