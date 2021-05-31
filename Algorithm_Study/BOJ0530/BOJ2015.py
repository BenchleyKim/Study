import sys
sys.stdin = open(".\Algorithm_Study\BOJ0530\BOJ2015","r")
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int,input().split()))
psum = []
psum.append(arr[0])
for i in range(1,N) :
    psum.append(psum[i-1] + arr[i])
hashMap = {}
for i in range(N) :
    if hashMap.get(psum[i]) :
        hashMap[psum[i]] += 1
    else :
        hashMap[psum[i]] = 1
ans = 0
for k in sorted(hashMap.keys()) :
    print(k)
    if hashMap.get(k-K) :
        ans += hashMap[k]

print(ans)
