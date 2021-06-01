import sys
sys.stdin = open("./Algorithm_Study/BOJ0419/BOJ5639","r")
input = sys.stdin.readline
n = input()
arr = []
while n != '' :
    n = int(n)
    arr.append(n)
    n = input()
print(arr)
tree = {a[0] : {'root' : -1}}

for node in arr :
    root = 50
    while tree[root] > node :
        if tree[root].get('left') :
            root = tree[root]['left']
        else :
            break
    while tree[root] < node :
        if tree[root].get('right') :
            root = tree[root]['right']
        else :
            




