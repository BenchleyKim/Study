import sys
from itertools import combinations
sys.stdin = open("./Algorithm_Study/2021Summer/src/com/company/BOJ1759/BOJ1759.in","r")
input = sys.stdin.readline

L, C = map(int, input().split())
arr = set(input().split())
all_case = list(combinations(arr, L))
mm = {"a","e","i","o", "u"}
check_m = arr & mm 
check_g = arr - mm

result = []

for case in all_case :
    case = set(case) 
    if len(case & check_m) >= 1 and len(case & check_g) >= 2:
        result.append("".join(sorted(list(case))))
result.sort()
for r in result :
    print(r)