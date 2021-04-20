import sys 
sys.stdin = open("./Algorithm_Study/0321/BOJ10828", "r")
input = sys.stdin.readline

N = int(input())
stack = []
for _ in range(N) :
    C = input().rstrip()
    if C == 'top' :
        if stack :
            print(stack[-1])
        else :
            print(-1)
        continue
    if C == 'size' :
        print(len(stack))
        continue
    if C == 'empty' : 
        if len(stack) == 0 :
            print(1)
        else :
            print(0)
        continue
    if C == 'pop' :
        if not stack :
            print(-1)
        else :
            print(stack.pop())
        continue
    
    C, K = C.split()
    
    if C == 'push' :
        stack.append(int(K))
        
