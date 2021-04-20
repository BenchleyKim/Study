import sys 
sys.stdin = open("./Algorithm_Study/BOJ0304/BOJ15650", "r")

n,m = map(int,sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
c = [False]*(n+1)
a = [0]*m
 
def go(index, start, n, m):
    if index == m:
        sys.stdout.write(' '.join(map(str,a))+'\n')
        return
    for i in range(0, n):
        if c[i]:
            continue
        c[i] = True
        a[index] = arr[i]
        go(index+1, i+1, n, m)
        c[i] = False
go(0,0,n,m)