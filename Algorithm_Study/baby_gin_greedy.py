# 입력 ( 6자리의 정수 값 )
input_str = str(input())

# 입력 테스트 예시 
# input_str = "667767"

# 예상 출력 True 

# RUN 인지 (3개가 연속된 값인지)  # Tripletes 인지 (3개가 같은 값인지)
def isGin(input_list):
    input_list.sort()
    # isRun
    if (input_list[2] + input_list[0]) == input_list[1] *2:
        if (input_list[2] - input_list[0]) == 2:
            return True
        # isTripletes 
        elif(input_list[2] - input_list[0]) == 0:
            return True
    return False

# 조합 lst : 입력 리스트 / n : 추출할 수  
def comb(lst,n):
	ret = []
	if n > len(lst): return ret
	
	if n == 1:
		for i in lst:
			ret.append([i])
	elif n>1:
		for i in range(len(lst)-n+1):
			for temp in comb(lst[i+1:],n-1):
				ret.append([lst[i]]+temp)

	return ret
def genLaca(lst, input_list):
    last_list = list(input_list)
    for i in lst:
        last_list.remove(i)
    return last_list

def solution(input_str):
    input_str = [int(i) for i in input_str]
    all_case = comb(input_str,3 )
    print(all_case)
    for test_case in all_case :
        if isGin(test_case):
            print(test_case)
            # 나머지 3개의 조합 찾기 
            last_case = genLaca(test_case, input_str)
            if isGin(last_case): 
                print(last_case)
                return True
    return False
        
    
print(solution(input_str))



# 6개 중에서 모든 3개의 조합을 추출

# 처음 3자리 중에서 맞으면 나머지 3 자리 중에서 추출해본다. 

#

# 출력 ( Baby-gin인지 True False )




