
def solution(gift_cards, wants) :
  check = {i:0 for i in range(100000)}
  for gift_num in gift_cards :
    check[gift_num] += 1
  cnt = 0
  for want in wants :
    if check[want] == 0 :
      cnt += 1
    else :
      check[want] -= 1
  return cnt 



print(solution([4, 5, 3, 2, 1],	[2, 4, 4, 5, 1]))
print(solution([5, 4, 5, 4, 5],	[1, 2, 3, 5, 4]))