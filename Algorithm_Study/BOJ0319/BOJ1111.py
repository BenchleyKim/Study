import sys
def solution(N, number):
    INF= sys.maxsize
    DP = [INF] * (number*N+1)
    DP[N] = 1
    for i in range(1,number*N+1):
      DP[i] = min(DP[i], DP[N] + DP[i-N])
      if i % N :
        pass
      else :
        DP[i] = min(DP[i], DP[N] * DP[i//N])
      DP[i//N] = min(DP[i//N], DP[i]+1)
    print(DP)
    answer = DP[number]
    return answer
print(solution(5, 12))