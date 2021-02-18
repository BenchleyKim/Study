import sys
sys.stdin = open('./Algorithm_study/0217/boj1074','r')
N , r, c = map(int, input().split())

l = 2**N
print(l)
count = 0
def search(n,row,col) :
  global count
  if n == 1 :
    print(count)
  else : 
    n -= 1
    if row >= 2**n :
      count += 4**n
      if col >= 2**n :
        count += 2**n 
        search(n,row,col)
      else :
        search(n,row,col)
    else :
      if col >= 2**n :
        count += 2**n 
        search(n,row,col)
      else :
        search(n,row,col)
search(l,r,c)

# M = [[i+j*(2**N) for i in range(2**N)] for j in range(2**N)]

# print(M)
# # print(M)
# target = r * (2**N) + c
# # print(target)
# count = 0
# def devideandconquer(arr, target,n) :
#   global count 
#   if n == 1 :
#     for ar in arr :
#       for a in ar :
#         if a == target : 
#           print(count)
#           return
#         count+=1
#   else :
#     # devide
#     n -= 1
#     uarr = arr[:2**n]
#     darr = arr[2**n:]
#     arr1 = []
#     arr2 = []
#     arr3 = []
#     arr4 = []
#     for ar in uarr :
#       arr1.append(ar[:2**n])
#       arr2.append(ar[2**n:])
#     for ar in darr :
#       arr3.append(ar[:2**n])
#       arr4.append(ar[2**n:])
#     devideandconquer(arr1,target,n)
#     devideandconquer(arr2,target,n)
#     devideandconquer(arr3,target,n)
#     devideandconquer(arr4,target,n)
# devideandconquer(M,target,N)
