from itertools import combinations
import string
def solution(orders, course):
  answer = []
  atoz = list(string.ascii_uppercase)
  for num in course :
    all_case = {case : 0 for case in combinations(atoz, num)}
    mx = 0
    for order in orders :
      subcases = combinations(list(sorted(order)),num)
      for sub in subcases :
        all_case[sub] += 1
        mx = max(mx, all_case[sub])
    for idx in all_case.keys() :
      if all_case[idx] >= 2 and all_case[idx] >= mx :
        answer.append("".join(idx))
  answer.sort()
  return answer





order = ["XYZ", "XWY", "WXA"]
course = [2,3,4]	
print(solution(order,course))