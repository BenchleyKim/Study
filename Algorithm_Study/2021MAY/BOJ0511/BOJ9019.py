
import sys
from collections import deque
sys.stdin = open(".\Algorithm_Study\BOJ0511\BOJ9019","r")
input = sys.stdin.readline

T = int(input())
def calD(n) :
    n *= 2
    if n > 9999 :
        n = n%10000
    return n
def calS(n) :
    n -= 1 
    if n < 0 :
        n = 9999
    return n 
def calL(n) :
    l = 0
    if n >= 1000 :
        l = n //1000
    n *= 10
    n += l
    n %= 10000
    return n 
def calR(n) :
    r = n % 10
    n //= 10 
    n += r*1000
    return n

print(calL(123))
print(calR(123))
print(calS(0))


for _ in range(T) :
    check = [0] * 10000
    A, B = map(int, input().split())
    queue = deque([(A,"")])
    while queue :
        node, arr = queue.popleft()
        if check[node] :
            continue
        if node == B :
            print(arr)
            break
        check[node] = 1
        queue.append((calD(node),arr+"D"))
        queue.append((calS(node), arr+"S"))
        queue.append((calL(node), arr+"L"))
        queue.append((calR(node), arr+"R"))


