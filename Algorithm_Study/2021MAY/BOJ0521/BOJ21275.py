import sys
sys.stdin = open(".\Algorithm_Study\BOJ0521\BOJ21275","r")
input = sys.stdin.readline

Xa , Xb = input().rstrip().split()
amx = 0 
for a in Xa :
    base = 0
    if a.isalpha() :
        base = ord(a) - ord('a') + 10
    else :
        base = int(a)
    amx = max(amx, base)

bmx = 0

for a in Xb :
    base = 0
    if a.isalpha() :
        base = ord(a) - ord('a') + 10
    else :
        base = int(a)
    bmx = max(bmx, base)
case = 0 
ans = []
INF = 2**63
print(amx, bmx)
for i in range(max(amx+1,2),36) :
    if int(Xa,i) >= INF :
        break
    for j in range(max(bmx+1,2),36) :
        if int(Xb,j) >= INF :
            break
        if i == j : 
            continue
        if int(Xa,i) == int(Xb,j) :
            ans = [int(Xa,i),i,j]
            case += 1
            continue
if case < 1 :
    print("Impossible")
elif case == 1 :
    for a in ans :
        print(a, end=' ')
else :
    print("Multiple")