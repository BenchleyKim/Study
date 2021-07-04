def solution(grid):
    answer = 0
    R , C = len(grid), len(grid[0])
    DP = [[0] * C for _ in range(R)]
    DP[0][0] = grid[0][0]
    for i in range(1, C) :
        DP[0][i] = DP[0][i-1] + grid[0][i]
    for i in range(1,R):
        DP[i][0] = DP[i-1][0] + grid[i][0]
    for i in range(1,R) :
        for j in range(1,C) :
            DP[i][j] = min(DP[i-1][j], DP[i][j-1]) + grid[i][j]
    answer = DP[i][j]
    return answer