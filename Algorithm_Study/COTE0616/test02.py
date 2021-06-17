import sys
sys.stdin = open(".\Algorithm_Study\COTE0616\\test02","r")
input = sys.stdin.readline

def main():
    # 이곳에 소스코드를 작성하세요.
    # Python3 만 지원됩니다.
    # pass는 삭제해도 됩니다.
    T = int(input())
    for t in range(T) :
        A, B, L = map(int, input().rstrip().split())
        farr = input().rstrip()
        rarr = farr[L::-1]
        
        A = list(f"{A:06}")
        B = list(f"{B:06}")
        for i in range(6) :
            diff = int(A[i]) - int(B[i])
            if diff < 0 :
                if farr[0] == '-' :
                    
            print(diff)
        


        
        print(A, B, L)
        print(farr)
        print(rarr)
    
main()