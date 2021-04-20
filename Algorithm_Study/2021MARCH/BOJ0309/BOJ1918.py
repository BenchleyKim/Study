import sys 
sys.stdin = open("./Algorithm_Study/BOJ0309/BOJ1918", "r")

S = sys.stdin.readline()
print(S)
prior = {'*':3,"/":3,"+":2,'-':2,'(':1,')':1}
stack = []
for s in S :
  print(stack)
  if s in prior.keys() :
    # 계산 처리
    if s == '(' :
      stack.append(s)
    elif s== ')' :
      while stack[-1] != '(' :
        print(stack.pop())
      stack.pop()
      
    else :
      tmp = []
      if stack :
        while stack and prior[stack[-1]] < prior[s] :
          tmp.append(stack.pop())
        if tmp : 
          stack.append(s)
          while tmp :
            stack.append(tmp.pop())
        else :
          stack.append(s)
      else :
        stack.append(s)

  else :
    print(s)
  
for s in stack :
  print(s)