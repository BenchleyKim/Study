import sys
from collections import deque 
sys.stdin = open(".\Algorithm_Study\BOJ0602\BOJ2346","r")
input = sys.stdin.readline

N = int(input())

arr = list(map(int,input().split()))
arr = list(enumerate(arr))
arr = deque(arr)

tmp = 0
while arr :
    while tmp > 0 :
        tmp -= 1 
        arr.append(arr.popleft())
    while tmp < 0 :
        tmp += 1 
        arr.appendleft(arr.pop())
    idx, node = arr.popleft()
    print(idx+1,end=' ')
    if node > 0 :
        tmp = node - 1 
    else :
        tmp = node 
    



