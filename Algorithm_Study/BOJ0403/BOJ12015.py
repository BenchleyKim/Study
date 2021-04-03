import sys
sys.stdin = open("./Algorithm_Study/BOJ0403/BOJ12015", "r")
input = sys.stdin.readline
 
N = int(input())
A = list(map(int, input().split()))
LIS = [0]
length = 0
# print(A)
for num in A:
    # print(num, LIS)
    if num > LIS[-1]:
        LIS.append(num)
        length += 1
    else:
        left = 0
        right = len(LIS)
 
        while right > left:
            mid = (left + right) // 2
 
            if LIS[mid] < num:
                left = mid + 1
            else:
                right = mid
        LIS[right] = num
print(length)