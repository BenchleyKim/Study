test_num = int(input())
test_list = []
for i in range(test_num):
    input_n, input_m = map(int, input().split())
    num_list = input().split()
    num_list = [int(i) for i in num_list] 
    test_list.append([input_n, input_m, num_list])


def betSum(idx, betsize, lst):
    oneside = int(betsize / 2)
    # print(sum(lst[idx-oneside:idx+oneside]))
    return sum(lst[idx-oneside:idx+oneside+1])

def findmax(betsize,lst):
    max = 0 
    oneside = int(betsize / 2)
    for i in range(len(lst)):
        if i-oneside <0 :
            pass
        elif i+oneside >= len(lst):
             pass
        else : 
            if betSum(i,betsize,lst) >= max:
                max = betSum(i,betsize,lst)
    return max

def findmin(betsize,lst,max):
    min = max
    oneside = int(betsize / 2)
    for i in range(len(lst)):
        if i-oneside < 0 :
            pass
        elif i+oneside >= len(lst):
            pass
        else : 
            if betSum(i,betsize,lst) <= min:
                min = betSum(i,betsize,lst)
    return min

def finddiff(betsize,lst):
    max_value = findmax(betsize, lst)
    min_value = findmin(betsize, lst, max_value)
    diff_value = max_value - min_value
    return diff_value


for i in range(test_num):
    # print(input_list[i])
    print(test_list[i][1])
    print("#%d %d"%(i+1, finddiff(test_list[i][1],test_list[i][2])))