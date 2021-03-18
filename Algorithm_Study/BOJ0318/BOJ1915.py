import sys
sys.stdin = open("./Algorithm_Study/BOJ0318/BOJ1915", "r")
input = sys.stdin.readline
n, m = map(int, input().split())
s = [[0 for i in range(m + 1)]]
for i in range(n): s.append([0] + list(input().strip()))
dp = [[0] * (m + 1) for i in range(n + 1)]
result = 0
for i in range(n + 1):
    for j in range(m + 1):
        if s[i][j] == "1": dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
for i in range(n + 1):
    for j in range(m + 1):
        result = max(result, dp[i][j])
print(result ** 2)