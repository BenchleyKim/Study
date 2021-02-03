
n = 100000
arr = []
for i in range(n+1):
  if i == 0 : arr.append(i)
  elif i == 1: arr.append(i)
  else : arr.append(arr[i-1]+arr[i-2])
print(arr[n])