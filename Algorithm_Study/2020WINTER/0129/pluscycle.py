n = int(input())

nn = n 
count = 0
while True :
  count += 1
  ln = nn // 10
  rn = nn % 10
  rr = (ln + rn) % 10
  nn = rn * 10 + rr
  if nn == n :
    break
print( count )