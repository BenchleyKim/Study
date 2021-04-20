import sys 
sys.stdin = open("./Algorithm_Study/BOJ0306/BOJ1991", "r")

N = int(sys.stdin.readline())
tree = {}
checkList = {}
for i in range(N) :
  root, left, right = sys.stdin.readline().split()
  tree[root] = [0,0]
  checkList[root] = 0
  if left != '.' :
    tree[root][0] = left
  if right != '.' :
    tree[root][1] = right

def preorder(root) :
  if checkList[root] :
    return
  checkList[root] = 1
  print(root,end='')
  if tree[root][0] != 0:
    preorder(tree[root][0])
  if tree[root][1] != 0:
    preorder(tree[root][1])

def inorder(root) :
  if checkList[root] :
    return
  checkList[root] = 1
  
  if tree[root][0] != 0:
    inorder(tree[root][0])
  print(root,end='')
  if tree[root][1] != 0:
    inorder(tree[root][1])

def postorder(root) :
  if checkList[root] :
    return
  checkList[root] = 1
  if tree[root][0] != 0:
    postorder(tree[root][0])
  if tree[root][1] != 0:
    postorder(tree[root][1])
  print(root,end='')

preorder('A')
print()
for c in checkList.keys():
  checkList[c] = 0

inorder('A')
print()
for c in checkList.keys():
  checkList[c] = 0

postorder('A')


