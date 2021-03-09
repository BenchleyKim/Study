import sys 
sys.stdin = open("./Algorithm_Study/0215/1085.txt", "r")
x,y,w,h= map(int, input().split())
print(min(int(abs(w-x)), x , y, int(abs(h-y))))