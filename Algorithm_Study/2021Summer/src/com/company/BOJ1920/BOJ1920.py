import sys
sys.stdin = open("./Algorithm_Study/2021Summer/src/com/company/BOJ1920/BOJ1920.in","r")
input = sys.stdin.readline

N = int(input())
arr = set(map(int, input().split()))
M = int(input())
karr = list(map(int, input().split()))

for k in karr :
    if k in arr :
        print(1)
    else :
        print(0)