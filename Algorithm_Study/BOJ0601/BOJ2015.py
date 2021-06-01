import sys
sys.stdin = open(".\Algorithm_Study\BOJ0601\BOJ2015","r")
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))
sum_arr = []
base = 0 
for a in arr :
    base += a 
    sum_arr.append(base)
cnt = 0
hash = {}
for a in sum_arr :
    if a == K : 
        cnt += 1
    if hash.get(a-K) :
        cnt += hash[a-K]
    if hash.get(a) :
        hash[a] += 1
    else :
        hash[a] = 1
print(cnt)


