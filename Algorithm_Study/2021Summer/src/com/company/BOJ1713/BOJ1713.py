import sys
from collections import deque
sys.stdin = open("./Algorithm_Study/2021Summer/src/com/company/BOJ1713/BOJ1713.in","r")
input = sys.stdin.readline

N = int(input())
K = int(input())
arr = list(map(int, input().split()))
check = {}
for a in arr :
    if a in check :
        check[a] += 1
        continue
    if len(check) < N :
        check[a] = 1 
    else :
        mx = 1000
        idx = 0
        for key in check.keys() :
            if check[key] < mx :
                idx = key
                mx = check[key]
        del check[idx]
        check[a] = 1

for a in sorted(check.keys()) :
    print(a, end=" ")


