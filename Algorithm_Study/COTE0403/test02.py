from itertools import combinations
def solution(needs, r) :
  comb_list = [ i for i in range(len(needs[0]))]
  print(comb_list)
  cases = list(combinations(comb_list,r))
  print(list(cases))
  mx = 0
  for case in cases :
    cnt = 0
    for need in needs :
      flag = True 
      for i in range(len(need)) :
        if need[i] == 1 :
          if i not in case :
            flag = False
            break
      if flag :
        cnt += 1
    mx = max(mx, cnt)
  return mx

print(solution([ [ 1, 0, 0 ], [1, 1, 0], [1, 1, 0], [1, 0, 1], [1, 1, 0], [0, 1, 1] ], 2))    

    

