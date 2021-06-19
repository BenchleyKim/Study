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

    def cal_entropy(diff) :
        result = 0 
        for d in diff :
            result += abs(d)
        return result 

    def filter_available(base , filter, idx) :
        for i in range(len(filter)) :
            if filter[i] == '+' :
                if diff[idx + i] == 9 :
                    return False 
                continue
            if filter[i] == '-' :
                if diff[idx + i] == 0 :
                    return False
                continue
            if filter[i] =='0' :
                continue
        return True

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

    T = int(input())
    for t in range(T) :
        answer = 0 
        A, B, L = map(int, input().rstrip().split())
        farr = input().rstrip()
        rarr = farr[L::-1]
        
        A = list(f"{A:06}")
        A = list(map(int, A))
        B = list(f"{B:06}")
        B = list(map(int, B))
        diff = cal_diff(A,B)
        idx = 0
        while True :
            if idx >= 6- L + 1 :
                break
            while diff[idx] != 0 :
                e1 , e2 = 81, 81
                if filter_available(A,farr, idx) :
                    c1 = cal_filter(A,farr,idx)
                    d1 = cal_diff(c1, B)
                    e1 = cal_entropy(d1)
                if filter_available(A,rarr,idx) :
                    c2 = cal_filter(A,rarr,idx)
                    d2 = cal_diff(c2,B)
                    e2 = cal_entropy(d2)
                if e1 == 81 and  e2 == 81 :
                    answer = - 1
                    break
                answer += 1
                print(e1, e2)
                print(diff)
                if e1 < e2 :
                    A = c1 
                    diff = d1
                else :
                    A = c2
                    diff = d2
            idx += 1
        for d in diff :
            if d != 0 : 
                answer = - 1
                break
        print(f"#{t+1} {answer}")
    
main()