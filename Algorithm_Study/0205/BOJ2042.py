N , M , K = map(int, input().split())
arr = []
for _ in range(N) :
    arr.append(int(input()))

for _ in range(M+K) :
    a ,b ,c = list(map(int, input().split()))
    if a == 1 :
        arr[b-1] = c
    elif a == 2:
        print(sum(arr[b-1:c]))



