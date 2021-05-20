
import sys
sys.stdin = open(".\Algorithm_Study\BOJ0520\BOJ1654","r")
input = sys.stdin.readline

k,n = map(int, input().split())
cable = [int(sys.stdin.readline()) for _ in range(k)]

left, right = 1, max(cable)

while left <= right:
    mid = (left + right) // 2
    print(left, mid, right)
    cnt = 0
    for c in cable:
        cnt += c // mid
    if cnt >= n:
        left = mid + 1
    else:
        right = mid - 1
print(right)