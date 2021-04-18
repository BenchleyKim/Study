import sys 
from itertools import combinations
sys.stdin = open("./Algorithm_Study/STD0418/test02", "r")
input = sys.stdin.readline

N = int(input())
arr = [ ]
for i in range(N) :
    arr.append(list(map(int, input().split())))
mn = sys.maxsize
for i in range(1,N+1) :
    cases = list(combinations(arr, i))
    for case in cases :
        sour = 1
        bitter = 0
        for element in case :
            sour *= element[0]
            bitter += element[1]
        diff = abs(sour - bitter) 
        mn = min(mn, diff)
print(mn)
