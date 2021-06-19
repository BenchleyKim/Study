import sys
sys.stdin = open("Algorithm_Study/COTE0616/Test02","r")
input = sys.stdin.readline

def main():
    # 이곳에 소스코드를 작성하세요.
    # Python3 만 지원됩니다.
    # pass는 삭제해도 됩니다.
    def cal_diff(left , right) :
        diff = []
        for i in range(6) :
            diff.append(int(left[i])-int(right[i]))
        return diff
    # print(cal_diff([0,0,0,5,5,5],[0,0,0,1,5,9]))

    def cal_entropy(diff,idx) :
        # result = 0 
        # for d in diff :
        #     result += abs(d)
        return abs(diff[idx])
    # print(cal_entropy([0,0,0,-4,0,4]))

    def filter_available(base , filter, idx) :
        for i in range(len(filter)) :
            if filter[i] == '+' :
                if base[idx + i] == 9 :
                    return False 
                continue
            if filter[i] == '-' :
                if base[idx + i] == 0 :
                    return False
                continue
            if filter[i] =='0' :
                continue
        return True
    # print(filter_available([0,0,0,5,5,5],"+-",3))

    def cal_filter(base, filter, idx) :
        result = []
        for i in range(idx) :
            result.append(base[i])
        for i in range(len(filter)) :
            if filter[i] == '+' : 
                result.append(base[idx + i] + 1)
                continue
            if filter[i] == '-' :
                result.append(base[idx + i] - 1)
                continue
            if filter[i] =='0' :
                result.append(base[idx+i])
                continue
        for i in range(idx+len(filter),6 ) :
            result.append(base[i])
        return result
    # print(cal_filter([0,0,0,5,5,5],"+-",3))
    T = int(input())
    for t in range(T) :
        A, B , L = map(int,input().split())
        F = input().rstrip()
        RF = F[::-1]
        
        A = list(map(int, f"{A:06}"))
        B = list(map(int, f"{B:06}"))
        F = tuple(F)
        # print(A, B, F)
        answer = 0 
        idx = 0 
        while True :
            if idx > 6 - L :
                break
            diff = cal_diff(A, B) 
            while diff[idx] != 0 :
                # print(A,B,diff)
                cE = cal_entropy(diff,idx)
                E1 = 10
                E2 = 10
                if filter_available(A,F,idx) :
                    C1 = cal_filter(A,F,idx)
                    D1 = cal_diff(C1,B)
                    E1 = cal_entropy(D1,idx)
                if filter_available(A,RF,idx) :
                    C2 = cal_filter(A,RF,idx)
                    D2 = cal_diff(C2,B)
                    E2 = cal_entropy(D2,idx)
                if E1 >= cE and E2 >= cE :
                    idx = 6
                    answer = -1
                    break
                answer += 1
                if E1 < E2 :
                    A = C1 
                    diff = D1 
                else :
                    A = C2 
                    diff = D2
            idx += 1
        idx = 5
        while True :
            if idx < L :
                break
            diff = cal_diff(A, B) 
            while diff[idx] != 0 :
                # print(A,B,diff)
                cE = cal_entropy(diff,idx)
                E1 = 10
                E2 = 10
                if filter_available(A,F,idx-L+1) :
                    C1 = cal_filter(A,F,idx-L+1)
                    D1 = cal_diff(C1,B)
                    E1 = cal_entropy(D1,idx)
                if filter_available(A,RF,idx-L+1) :
                    C2 = cal_filter(A,RF,idx-L+1)
                    D2 = cal_diff(C2,B)
                    E2 = cal_entropy(D2,idx)
                if E1 >= cE and E2 >= cE :
                    idx = 0
                    answer = -1
                    break
                answer += 1
                if E1 < E2 :
                    A = C1 
                    diff = D1 
                else :
                    A = C2 
                    diff = D2
            idx -= 1
        # print(diff)
        for d in diff :
            if d != 0 :
                answer = -1 
                break
        print(f"#{t+1} {answer}")
    
main()