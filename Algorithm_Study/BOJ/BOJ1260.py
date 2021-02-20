import sys 
sys.stdin = open("./Algorithm_Study/BOJ/BOJ1260", "r")

N, M , V = map(int, input().split())
Graph = { }
for _ in range(M) :
  a, b = map(int, input().split())

