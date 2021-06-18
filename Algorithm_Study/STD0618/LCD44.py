from typing import List

class Solution:
    
    def isMatch(self, s, p):
        length = len(s)
        if len(p) - p.count('*') > length:
            return False
        dp = [True] + [False]*length
        for i in p:
            print(dp)
            if i != '*':
                for n in reversed(range(length)):
                    dp[n+1] = dp[n] and (i == s[n] or i == '?')
            else:
                for n in range(1, length+1):
                    dp[n] = dp[n-1] or dp[n]
            dp[0] = dp[0] and i == '*'
        return dp[-1]



solutin = Solution()

s = "aa"
p = "a"
print(solutin.isMatch(s,p))
s = "aa"
p = "*"
print(solutin.isMatch(s,p))

s = "cb"
p = "?a"
print(solutin.isMatch(s,p))

s = "adceb"
p = "*a*b"
print(solutin.isMatch(s,p))

s = "acdcb"
p = "a*c?b"
print(solutin.isMatch(s,p))

s= ""
p = "******"
print(solutin.isMatch(s,p))
