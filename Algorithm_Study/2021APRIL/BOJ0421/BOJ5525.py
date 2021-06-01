import sys
sys.stdin = open("./Algorithm_Study/BOJ0421/BOJ5525","r")
input = sys.stdin.readline

N = int(input())
M = int(input())
s = input()
i = cnt = p = 0 
while i < M-2:
    if s[i] == 'I' and s[i+1] == 'O' and s[i+2] == 'I':
        i += 2
        p += 1
        if p == N:
            p -= 1
            cnt += 1    
    else:
        i += 1
        p = 0
print(cnt)