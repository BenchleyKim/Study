import sys
sys.stdin = open("./Algorithm_Study/BOJ0416/BOJ2448","r")

N = int(input())
tmp = N//3
k = 0 
while tmp > 1 :
    tmp //= 2
    k += 1
print(k) 
def triangle(left, right) :
    if right - left == 5 :
        print(" " * left + " "* 2 + "*")
        print()
        print(" "* left +" "+"* *")
        print()
        print(" "* left +"*****")
        return
    else :
        triangle(((right-left)//4)*2,((right-left)//4)*3)
        triangle(0,(right-left)//2)
        triangle((right-left)//2,right)

triangle(0,48)