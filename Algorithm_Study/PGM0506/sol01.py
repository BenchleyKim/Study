

def solution(S):
    N = len(S)
    tuples = []
    node = []
    nums = ""
    for i in range(1,N-1) :
        if S[i] == '{' :
            node = []
            continue
        if S[i] == '}' :
            tuples.append(node)
            continue
        if S[i] == ',' :
            node.append(int(nums))
            nums = ''
            continue
        nums += S[i]
    tuples[-1].append(int(nums))
    tuples = sorted(tuples, key = lambda x : len(x))
    check = set()
    answer = []
    for tu in tuples :
        for element in tu :
            if element in check :
                continue
            check.add(element)
            answer.append(element)
    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{20,111},{111}}"))
print(solution("{{123}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))