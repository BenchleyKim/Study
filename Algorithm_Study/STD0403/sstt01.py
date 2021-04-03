import sys 
sys.stdin = open("./Algorithm_Study/STD0403/sstt01", "r")
input = sys.stdin.readline
N = int(input())

left = 0
right = 1
cnt = 0
while left <= N :
    print(left, right) 
    cnt += 1
    left = right + 1
    right = left + 6 * cnt -1 
    
print(cnt)
