check = { 3: 1, 1:2, 2:1}
print(sorted(check,key=lambda x:(check[x],x)))
arr = [0,1,2,3]
print(arr[:2])
print(arr[4:])
for idx in range(1,len(arr)+1):
    print(idx-1, arr[idx:])
