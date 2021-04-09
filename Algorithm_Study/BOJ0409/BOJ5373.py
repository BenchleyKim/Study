import sys
sys.stdin = open("./Algorithm_Study/BOJ0409/BOJ5373", "r")
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(input().split())
    print(arr)


