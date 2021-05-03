import sys 
import re
sys.stdin = open(".\Algorithm_Study\BOJ0503\BOJ9935","r")
input = sys.stdin.readline

base = input().rstrip()
bomb = input().rstrip()
flag = re.search(bomb, base)

while flag :
    result = re.sub(bomb,'',base)
    base = result
    flag = re.search(bomb, base)
if len(base) == 0 :
    print('FRULA')
else :
    print(base)
