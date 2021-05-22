import sys
sys.stdin = open(".\Algorithm_Study\BOJ0522\BOJ1275","r")
input = sys.stdin.readline

N ,Q = map(int, input().split())
arr = list(map(int, input().split()))
segTree = []
for i in range(Q) :
    x ,y ,a,b  = map(int, input().split())