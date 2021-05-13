from os import rename
import sys
sys.stdin = open(".\Algorithm_Study\BOJ0513\BOJ14657","r")
input = sys.stdin.readline

N, T = map(int, input().split())
print(N,T)
graph = {}
for i in range(N-1) :
    A, B, W = map(int, input().split())
    if graph.get(A) :
        graph[A][B] = W
    else :
        graph[A] = {B:W}
    if graph.get(B) :
        graph[B][A] = W
    else :
        graph[B] = {A:W}
print(graph)