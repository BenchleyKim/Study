import sys
from itertools import permutations
sys.stdin = open("./Algorithm_Study/BOJ0417/BOJ1107","r")
input = sys.stdin.readline

N = input().rstrip()
L = len(N)
N = int(N)

M = int(input())
arr = list(map(int,input().split()))

button = list(range(10))
print(button)
for i in range(M) :
    button.remove(arr[i])
print(button)
print(N)
print(L)
current = abs(N- 100) 
mn = abs(N-100)
# for l in range(L-1,L+2) :
#     button_list = button * l
#     cases = list(permutations(button_list,l))
#     for case in  cases :
#         print(case)
