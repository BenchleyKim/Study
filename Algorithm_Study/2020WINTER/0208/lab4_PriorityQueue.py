# N번의 연산을 하는 프로그램을 작성합니다.
# 연산은 P 연산과 G 연산이 있습니다. 
# P < 숫자 > 연산은 < 숫자 >를 우선순위 큐에 넣습니다.
# G 연산은 우선순위 큐에서 가장 작은 값을 하나 빼내고 그 내용을 출력합니다. 

# 입력 ) 
# 1 ) N 을 입력합니다. 
# 2 ) N개의 연산이 한줄에 하나씩 나열됩니다. 

# 입력 예시 ) 
# 10 
# P 7 
# P 4
# P 10 
# G
# P 8
# P 2 
# P 5
# G
# G
# G

# 출력예)
# 4
# 2
# 5


n = int(input())

heap = [0]
def insert(data) : 
    heap.append(data)
    currentIdx = len(heap) -1
    while currentIdx >= 0 : 
        parentIdx = currentIdx  // 2
        if parentIdx >= 0 and heap[parentIdx] > heap[currentIdx] :
            heap[currentIdx], heap[parentIdx] = heap[parentIdx], heap[currentIdx]
            currentIdx = parentIdx
        else : 
            break
def popHeap() : 
    result = heap[1]
    heap[1] = heap.pop()
    temp = heap[1]
    r = 1
    while True :
        if temp < heap[2*r] and temp < heap[2*r+1] :
            break
        if temp > heap[2*r+1] :
            heap[r] , heap[2*r+1] = heap[2*r+1], heap[r]
            r += 1
            continue
        if temp > heap[2*r] :
            heap[r] , heap[2*r] = heap[2*r], heap[r]
            r += 1
            continue
        
    print(heap)
    return result
results = []
for _ in range(n) :
    Q = input()
    for q in Q : 
      if q == 'P' : insert(int(Q.split()[1])) ;
      elif q == 'G' : 
          results.append(popHeap()) 
for i in results :
    print(i)



      