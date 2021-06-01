

import sys
from collections import deque

sys.stdin = open(".\Algorithm_Study\BOJ0510\BOJ21740","r")
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
prior = {0:0,1:1,2:2,5:5,6:9,8:8,9:6}
def change(n) :
    n = str(n)
    ans = deque()
    for ele in n :
        ele = int(ele)
        ans.appendleft(prior[ele])
    while ans :
        if ans[0] == 0 :
            ans.popleft()
        else :
            break
    return int("".join(map(str, ans)))
        

arr = sorted(arr, key= lambda x : change(x))
arr.append(arr[-1])
for a in arr :
    print(a, end='')
