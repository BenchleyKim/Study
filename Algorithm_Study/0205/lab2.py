# arr = [1,2,5,6,2,4,3,7]
N , M , K = map(int, input().split())
arr = []
for _ in range(N) :
    arr.append(int(input()))
sumArr = []
for idx, a in enumerate(arr) :
    if idx % 2 : sumArr.append(sumArr[-1]+a); continue
    sumArr.append(a)
print(sumArr)


for _ in range(K+M) :
    c , a, b = map(int, input().split())
    if c == 1 :
        diff = 0
        if (a-1) % 2 : 
            diff = arr[a-1] - b 
            arr[a-1] = b
            sumArr[a-1] += diff
        else : 
            diff = arr[a-1] - b
            arr[a-1] = b
            sumArr[a-1] += diff
        continue
    if c== 2:
        s = (a - 1) // 2 
        e = (b - 1) // 2
        sum = 0
        for i in range(s+1,e+1) :
            sum += sumArr[2*i-1]
        if (a) % 2 : sum += arr[a-1]
        if (b) % 2 : sum += arr[b-1] 
        print(sum)
    print(sumArr)
    print(arr)

        
# [1,2,3,4,5] -> [1,2,6,4,5] -> [1,2,6,4,2]