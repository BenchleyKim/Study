
import sys
sys.stdin = open(".\Algorithm_Study\BOJ0520\BOJ11047","r")
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [ ]
for i in range(N) :
    arr.append(int(input()))
ans = 0 
while K > 0 :
    tmp = arr.pop()
    cnt, K = divmod(K,tmp)
    ans += cnt
print(ans)
