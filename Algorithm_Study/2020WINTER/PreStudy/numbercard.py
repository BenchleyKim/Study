# 0부터 9까지 주어진 카드 N개

# 가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력하는 프로그램을 만든다.

# 단 카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력한다. 

# 테스트 케이스 개수 T
test_num = int(input())

# 정수를 문자열로 바꿔줌 
def int2str(input_int):
    result_list = []
    while input_int > 0 :
        extract_int = input_int % 10
        input_int = int(input_int / 10)
        result_list.append(extract_int)
    return result_list

# 테스트 수 만큼 입력 받고 리스트에 저장한다. 
test_case = []
for i in range(test_num):
    card_num = int(input())
    card_list = int(input())
    card_list = int2str(card_list)
    test_case.append(card_list)
def findMany(lst):
    lst.sort()
    max_count = 0 
    max_num = 0 
    for i in lst :
        if lst.count(i) >= max_count :
            max_count = lst.count(i)
            max_num = i
    return [max_num, max_count]



for i in range(test_num):
    result = findMany(test_case[i])
    print("#%d %d %d"%(i+1, result[0], result[1] ))
    # print(test_case[i])




