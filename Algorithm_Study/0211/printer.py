priorities = [2, 1, 3, 2]
location = 1

def solution(priorities, location):
    queue = priorities
    stack = sorted(priorities)
    count = 0
    while True :
        tmp = queue.pop(0)
        if tmp < stack[-1] :
            queue.append(tmp)
            if location == 0 :
                location = len(queue)
        else : 
            count += 1
            stack.pop()
            if location == 0 :
                return count
        location -= 1
      

print(solution(priorities, location))