

# 첫 줄에 테스트 케이스 수 T가 주어진다.
case_num = int(input())
input_list = []
# 각 케이스의 첫 줄에 양수 개수 N이 주어진다
for i in range(case_num):
    list_num = int(input())
    # 다음줄에 N개의 양수가 ai가 주어진다. 
    case_list = input().split()
    case_list = [int(j) for j in case_list]
    input_list.append([list_num,case_list])
for i in input_list:
    print(i)

# 가장 큰 수와 가장 작은 수의 차이를 출력한다. 
def solution(input_list):
    result_list = []
    for i in input_list:
        list_num = i[0]
        case_list = i[1]
        for j in range(list_num-1):
            for k in range(list_num-j-1):
                print(str(j),str(k))
                if case_list[k]>case_list[k+1]:
                    temp = case_list[k]
                    case_list[k]=case_list[k+1]
                    case_list[k+1] = temp
        diff = case_list[list_num-1]-case_list[0]
        result_list.append(diff)
    return result_list


answer = solution(input_list)

# 출력 은 #(케이스 번호) 를 출력한 뒤 답을 출력한다. 
for i in range(case_num):
    print("#%d %d"%(i+1,answer[i]))