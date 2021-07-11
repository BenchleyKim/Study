answer = []
for i in range(100,301) :
    str1  = str(i)
    flag = True
    for c in str1 :
        if int(c) % 2 :
            flag = False
            break
    if flag :
        answer.append(str1)
    
print(",".join(answer))