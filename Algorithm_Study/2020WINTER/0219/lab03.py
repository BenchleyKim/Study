import sys 
sys.stdin = open("./Algorithm_Study/0219/lab03test", "r")
N = int(input())
arrA = list(map(int, input().split()))
A = 1 
for a in arrA :
  A *= a
M = int(input())
arrB = list(map(int, input().split()))
B = 1 
for b in arrB :
  B *= b
def Euclidean(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    
    return a
print("{0:09d}".format(Euclidean(A,B)%1000000000))
