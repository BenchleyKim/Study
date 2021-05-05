

def solution(gems):
    cat = {}
    l = 0
    h = 0
    for idx, gem in enumerate(gems) :
        if cat.get(gem) :
            cat[gem] = idx
            continue
        else :
            cat[gem] = idx
            h = idx
    print(cat)
    answer = []
    return answer


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))