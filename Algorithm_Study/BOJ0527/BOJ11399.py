import sys
sys.stdin = open(".\Algorithm_Study\BOJ0527\BOJ11399","r")
input = sys.stdin.readline


N = int(input())
arr = list(map(int, input().split()))
arr.sort()
ans = 0
p = 0
for i in arr :
    p = p + i 
    ans += p 
print(ans)

