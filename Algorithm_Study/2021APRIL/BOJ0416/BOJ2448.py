import sys
import math
sys.stdin = open("./Algorithm_Study/BOJ0416/BOJ2448","r")

def draw(cal):
    for i in range(len(stars)):
        stars.append(stars[i] + stars[i])
        stars[i] = ('   ' * cal + stars[i] + '   ' * cal)


stars = ['  *   ', ' * *  ', '***** ']
N = int(input())

iter = int(math.log(N // 3, 2))
print(iter)

for i in range(iter):
    draw(int(pow(2, i)))
    print(stars)

for i in range(N):
    print(stars[i])