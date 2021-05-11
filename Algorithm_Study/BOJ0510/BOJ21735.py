import sys

sys.stdin = open(".\Algorithm_Study\BOJ0510\BOJ21735","r")
input = sys.stdin.readline

N, M = map(int, input().split())

arr = list(map(int, input().split()))
arr = [0]+arr
ans = 1
def dfs(i, snow ,m) :
    global ans
    ans = max(snow, ans)
    if i > N :
        ans = max(snow, ans)
        return
    snow += arr[i]
    ans = max(snow, ans)
    if m == M :
        return
    if i >= N :
        return
    
    dfs(i+1,snow, m+1)
    dfs(i+2, snow//2, m+1)
    
dfs(0,1,0)
print(ans)