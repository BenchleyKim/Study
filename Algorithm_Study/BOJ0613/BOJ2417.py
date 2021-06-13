import sys
import math
sys.stdin = open(".\Algorithm_Study\BOJ0613\BOJ2417","r")
input = sys.stdin.readline

N = int(input())
print(math.ceil(N**(1/2)))



