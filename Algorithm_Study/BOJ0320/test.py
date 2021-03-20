import sys

def apart(k, n):
    result = 0
    if k == 0:
        return n
    elif n == 1:
        return n
    else:
        result += apart(k-1, n) + apart(k, n-1)
        return result

a = int(input())

for i in range(a):
    x = int(sys.stdin.readline())
    y = int(sys.stdin.readline())
    
    print(apart(x,y))