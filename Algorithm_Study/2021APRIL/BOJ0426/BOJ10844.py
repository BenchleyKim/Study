import sys 
sys.stdin = open(".\Algorithm_Study\BOJ0426\BOJ10844","r")
input = sys.stdin.readline
N = int(input())

DP = [[0]*1024 for i in range(10)]
for i in range(1,10) :
    DP[i][1<<i] = 1
for i in range(1, N) :
    nextDP = [[0]*1024 for i in range(10)]
    for e in range(10) :
        for b in range(1024) :
            if e < 9 :
                nextDP[e][b|(1<<e)] =( nextDP[e][b|(1<<e)] + DP[e+1][b]) % 1000000000
            if e > 0 :
                nextDP[e][b|(1<<e)] =( nextDP[e][b|(1<<e)] + DP[e-1][b]) % 1000000000
    DP = nextDP

print(sum([DP[i][1023] for i in range(10)])%1000000000)