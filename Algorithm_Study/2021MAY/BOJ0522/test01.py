

arr = list(map(int,input().split()))
mn  = 100
mx = max(arr)
1 1 2 3

for i in range(mx) :
    s = 0
    for a in arr :
        s += abs(a-i)
    mn = min(mn,s)
print(mn)