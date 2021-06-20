import sys 
input = sys.stdin.readline
def main():
    T = int(input())
    for t in range(T) :
        N, K = map(int, input().split())
        board = []
        for k in range(K) :
            board.append(list(input().rstrip()))
        mxsize =  K
        DP = [[mxsize] * N for _ in range(K)]

        '''
        Top-Down
        '''

        for n in range(N) :
            if board[0][n] == '1' :
                DP[0][n] = 0 
                continue
            for k in range(1,K) :
                if board[k][n] =='1' :
                    DP[0][n] = min(DP[0][n], k ,K - k )

        for k in range(1,K) :
            for n in range(N) :
                if board[k][n] == '1' :
                    DP[k][n] = 0
                    continue
                DP[k][n] = min(DP[k][n],DP[k-1][n]+1)
        # for d in DP :
        #     print(d)
        # print()

        '''
        Botton-Up
        '''
        for n in range(N) :
            if board[K-1][n] == '1' :
                DP[K-1][n] = 0
                continue
            DP[K-1][n] = min(DP[K-1][n] , DP[0][n] + 1)
        for k in range(K-2, -1,-1) :
            for n in range(N) :
                if board[k][n] == '1' :
                    DP[k][n] = 0 
                    continue
                DP[k][n] = min(DP[k][n],DP[k+1][n]+1)
        mn = mxsize
        for d in DP :
            # print(d)
            mn = min(mn, sum(d))
        print(f"#{t+1} {mn} ")
        
            
    
main()