
bridge_length = 2
weight = 10
truck_weights = 	[7,4,5,6]

queue = truck_weights
current = []
count = 1
while len(queue ) > 0 :
    count += bridge_length
    current.append(queue.pop(0))
    if len(queue) == 0 :
        break
    sub = 0
    while sum(current) + queue[0] <= weight :
        current.append(queue.pop(0))
        sub += 1
        if len(queue) == 0 :
            break
    current = []
    count += sub

print(count)