import sys
sys.stdin = open(".\Algorithm_Study\BOJ0511\BOJ17219","r")
input = sys.stdin.readline

N, M = map(int, input().split())
hashmap = {}
for i in range(N) :
    Address, Password = input().rstrip().split()
    hashmap[Address] = Password
for i in range(M) :
    Address = input().rstrip()
    print(hashmap[Address])
    



