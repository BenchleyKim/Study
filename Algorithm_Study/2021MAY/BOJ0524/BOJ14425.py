import sys
sys.stdin = open(".\Algorithm_Study\BOJ0524\BOJ14425","r")
input = sys.stdin.readline

N, M = map(int, input().split())
hashmap = {}
for i in range(N) :
    tmp = input().rstrip()
    hashmap[tmp ] = 1
ans =  0 
for i in range(M) :
    tmp = input().rstrip()
    if hashmap.get(tmp) :
        ans += 1
print(ans)

