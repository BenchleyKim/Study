import sys
from collections import deque
sys.stdin = open("./Algorithm_Study/BOJ0421/BOJ5430","r")
input = sys.stdin.readline

T = int(input())
for t in range(T):
    P = input().rstrip()
    N = int(input())
    src_arr = input().rstrip()
    src_arr = src_arr[1:-1]
    src_arr = src_arr.split(',')
    arr = deque()
    for a in src_arr :
        if a.isdigit() :
            arr.append(a)

    # print(arr)
    errorFlag = False
    reverseFlag = False
    for p in P :
        if p == 'R' :
            reverseFlag = not reverseFlag
        elif p == 'D' :
            if len(arr) == 0 :
                errorFlag = True
                break
            if reverseFlag :
                arr.pop()
            else :
                arr.popleft()
    if errorFlag :
        print("error")
    else :
        if reverseFlag :
            s = ','.join(list(reversed(arr)))
            
        else :
            s = ','.join(list(arr))
        print('['+s+']')




