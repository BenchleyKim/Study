
import time

current_time = time.time()
n = 10000
arr = []
for i in range(n+1):
  if i == 0 : arr.append(i)
  elif i == 1: arr.append(i)
  else : arr.append(arr[i-1]+arr[i-2])
print(arr[n])
print(current_time - time.time())
current_time = time.time()
def fibo(n):
    sqrt_5 = 5 ** (1/2)
    ans = (1 / sqrt_5 * ( ((1 + sqrt_5) / 2) ** n  - ((1 - sqrt_5) / 2) ** n )) % 1000000009
    return int(ans)

print(fibo(n))
print(current_time - time.time())

if arr[n] == fibo(n):
  print("right!")
