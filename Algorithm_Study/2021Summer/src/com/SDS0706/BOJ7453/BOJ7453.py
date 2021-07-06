import sys
sys.stdin = open("./Algorithm_Study/2021Summer/src/com/SDS0706/BOJ7453/BOJ7453.in","r")
input = sys.stdin.readline

N = int(input())

A , B , C, D = [[]for i in range(4)]
for i in range(N) :
    a,b,c,d= map(int, input().split())
    A.append(a) , B.append(b) , C.append(c) , D.append(d)

left_dict = {}
for i in range(N) :
    for j in range(N) :
        left_key = A[i] + B[j]
        if left_key in left_dict :
            left_dict[left_key] += 1
        else :
            left_dict[left_key] = 1
answer = 0 

for c in C :
    for d in D :
        if -(c+d) in left_dict :
            answer += left_dict[-(c+d)]

print(answer)