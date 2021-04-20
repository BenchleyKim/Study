import sys
import collections
sys.stdin = open("./Algorithm_Study/BOJ0325/BOJ12852", "r")

input = sys.stdin.readline

N = int(input())
INF = sys.maxsize
heap = collections.deque([[N]])
while heap :
  sequence = heap.popleft()
  node = sequence[0]
  if node == 1 :
    print(len(sequence)-1)
    for i in range(len(sequence)-1,-1,-1):
      print(sequence[i],end=' ')
    break
  if node % 3 == 0 :
    heap.append([node//3]+sequence)
  if node % 2 == 0 :
    heap.append([node//2]+sequence)
  heap.append([node-1]+sequence)



