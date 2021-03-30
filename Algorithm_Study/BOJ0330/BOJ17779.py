import sys 
sys.stdin = open("./Algorithm_Study/BOJ0330/BOJ17779", "r")
input = sys.stdin.readline
N = int(input())
A = []
for _ in range(N) :
  A.append(list(map(int, input().split())))
