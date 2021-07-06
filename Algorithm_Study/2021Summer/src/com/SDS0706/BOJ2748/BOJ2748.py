import sys
sys.stdin = open("./Algorithm_Study/2021Summer/src/com/SDS0706/BOJ2748/BOJ2748.in","r")
input = sys.stdin.readline

N = int(input())
cnt = 0 
f, s = 0, 1
while cnt < N :
    f , s = s , f+s
    cnt += 1

print(f)