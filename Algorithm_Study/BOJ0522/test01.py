

arr = list(map(int,input().split()))
mn  = 100
mx = max(arr)

for i in range(mx) :
    s = 0
    for a in arr :
        s += abs(a-i)
    mn = min(mn,s)
print(mn)