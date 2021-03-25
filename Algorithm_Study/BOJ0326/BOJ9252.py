import sys
sys.stdin = open("./Algorithm_Study/BOJ0326/BOJ9252", "r")
input = sys.stdin.readline
str1 = input().rstrip()
str2 = input().rstrip()
print(str1, str2) 
DP = [[0] * len(str1) for _ in range(len(str2))]
for i in range(len(str1)) :
  for j in range(len(str2)) :
     