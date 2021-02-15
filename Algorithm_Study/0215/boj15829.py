import sys 
sys.stdin = open("./Algorithm_Study/0215/15829", "r")
# L = int(input())
# S = input()
# r= 31
# M = 1234567891
# result = 0
# for i in range(L) :
#   result += (ord(S[i])-96)*((r**i)%M)
# print(result)

L = int(input())
string = input()
answer = 0
for i in range(L):
    answer += (ord(string[i])-96) * (31 ** i) #아스키 코드 값을 돌려주는 ord함수
print(answer % 1234567891)
# L = int(input())
# S = input()
# r= 31
# M = 1234567891
# result = 0
# for e, s in enumerate(S) :
#   i = ord(s)-96%M
#   b =r**e %M
#   result += (i*b)
# print(result)

