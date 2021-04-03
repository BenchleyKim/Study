import sys 
import math
sys.stdin = open("./Algorithm_Study/STD0403/sstt02", "r")
input = sys.stdin.readline
# 첫째 줄에 시험장의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다.

# 둘째 줄에는 각 시험장에 있는 응시자의 수 Ai (1 ≤ Ai ≤ 1,000,000)가 주어진다.

# 셋째 줄에는 B와 C가 주어진다. (1 ≤ B, C ≤ 1,000,000)

# 총 감독이 커버 가능한 수는 B , 부감독이 커버가능한 수는 C 

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
count  = 0
for i in range(N) :
    if A[i] <= B : 
        count+= 1
        continue
    count += math.ceil((A[i]-B)/C)+1
print(count)
