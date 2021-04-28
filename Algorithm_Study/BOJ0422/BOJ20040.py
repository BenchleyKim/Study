import sys
sys.stdin = open("./Algorithm_Study/BOJ0422/BOJ20040","r")
input = sys.stdin.readline

N, M = map(int, input().split())

check = [i for i in range(N)]
ans = 0
for i in range(1,M+1) :
    a, b = map(int, input().split())
    ra , rb = a, b
    while ra != check[ra] :
        ra = check[ra]
    check[a] = ra
    while rb != check[rb] :
        rb = check[rb]
    check[b] = rb
    if check[a] == check[b] :
        ans = i
        break

    check[ra] = check[rb] = min(ra,rb)
print(ans)