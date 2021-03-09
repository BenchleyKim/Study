# nh = list(map(int, input().split()))
nh = [7, 2, 1, 4, 5, 1, 3, 3]
n = nh[0]
hist = nh[1:]
middle = n // 2

def devideAndConquer(left,right) :
  if left == right : return hist[left]

  # Devide
  mid = (left + right ) // 2
  max = devideAndConquer(left, mid)
  rmax = devideAndConquer(mid, right)
  if rmax > max : max = rmax
  # Conquer
  min = hist[mid]
  if 



