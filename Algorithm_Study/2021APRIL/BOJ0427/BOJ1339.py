import sys 

sys.stdin = open(".\Algorithm_Study\BOJ0427\BOJ1339","r")
input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N) :
    arr.append(list(input().rstrip()))

alpha = {}
for i in range(N) :
    for j in range(len(arr[i])) :
        if alpha.get(arr[i][j]) :
            alpha[arr[i][j]] += 10**(len(arr[i])-j-1)
            continue
        alpha[arr[i][j]] = 10**(len(arr[i])-j-1)

res = sorted(alpha.items(), key=(lambda x : x[1]), reverse= True)
ans = 0
for idx, d in enumerate(res) :
    k, v = d
    ans += v * (9-idx)
print(ans)

