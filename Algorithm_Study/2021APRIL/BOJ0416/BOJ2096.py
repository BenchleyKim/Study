import sys
sys.stdin = open("./Algorithm_Study/BOJ0416/BOJ2096","r")
input = sys.stdin.readline

N = int(input())

INF = sys.maxsize

mxDP = [[0]*3 for _ in range(2)]
mnDP = [[INF]*3 for _ in range(2)]

arr1 = list(map(int,input().split()))
mxDP[0] = arr1[:]
mnDP[0] = arr1[:]
for i in range(1,N) :
    arr = list(map(int, input().split()))
    
    mxDP[1][0] = max(mxDP[0][0],mxDP[0][1]) + arr[0]
    mxDP[1][2] = max(mxDP[0][2],mxDP[0][1]) + arr[2]
    mxDP[1][1] = max(mxDP[0][0],mxDP[0][1],mxDP[0][2]) + arr[1]
    mxDP[0][0],mxDP[0][1],mxDP[0][2] = mxDP[1][0],mxDP[1][1],mxDP[1][2]

    mnDP[1][0] = min(mnDP[0][0],mnDP[0][1]) + arr[0]
    mnDP[1][2] = min(mnDP[0][2],mnDP[0][1]) + arr[2]
    mnDP[1][1] = min(mnDP[0][0],mnDP[0][1],mnDP[0][2]) + arr[1]
    mnDP[0][0],mnDP[0][1],mnDP[0][2] = mnDP[1][0],mnDP[1][1],mnDP[1][2]
# print(mnDP)
# print(mxDP)
print(max(mxDP[0]),min(mnDP[0]))
