import sys
sys.stdin = open(".\Algorithm_Study\BOJ0611\BOJ18866","r")
input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N) :
    arr.append(list(map(int, input().split())))
print(arr)
