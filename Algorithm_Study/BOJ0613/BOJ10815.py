import sys

sys.stdin = open(".\Algorithm_Study\BOJ0613\BOJ10815","r")
input = sys.stdin.readline

N = int(input())
narr = map(int, input().split())
M = int(input())
marr = map(int, input().split())

check = [0] * 20_000_002
for i in narr :
    if i >= 0 :
        check[i] = 1 
        continue
    check[i] = -1 

for i in marr :
    if check[i] * abs(i) == i :
        print(1, end=' ')
    else :
        print(0, end=' ')
