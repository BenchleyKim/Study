import sys 
import re
sys.stdin = open("./Algorithm_Study/COTE0402/test01", "r")
input = sys.stdin.readline
p = re.compile('[a-z]|[A-Z]|[0-9]|[._-]')
d = re.compile('[.]{2,}')


def check(id) :
  if len(id) >= 3 and len(id) <=15 :
    pass
  else : return False
  if id[0] == '.' or id[-1] == '.' :
    return False
  m = d.findall(id)
  print(m)
  if len(m) > 0 :
    return False
  m = p.findall(id)
  if len(m) != len(id) :
    return False
  return True
def solution(new_id):
  answer = new_id
  # print(check(new_id))
  while not check(answer) :
    answer = "".join(answer)
    print(answer)
    # 1단계 소문자 변환
    answer = answer.lower()
    # 2단계 규칙에 안맞는 문자 제거
    answer = "".join(p.findall(answer))
    print(answer)
    # 마침표 2개 1개로 치환
    answer = re.sub('[.]{2,}','.',answer)
    if answer.startswith('.'):
      answer = "".join(answer[1:])
    if answer.endswith('.') :
      answer = "".join(answer[:-1])
    if len(answer) == 0 :
      answer = 'a'
    if len(answer) >= 16 :
      answer = "".join(answer[:15])
      if answer.endswith('.') :
        answer = "".join(answer[:-1])
    while len(answer) <= 2 :
      answer = "".join(answer + answer[-1])
  return answer
    

print(solution("...!@BaT#*..y.abcdefghijklm"))