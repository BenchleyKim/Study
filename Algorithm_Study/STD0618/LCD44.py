from typing import List

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_idx = 0 
        p_idx = 0
        result = False
        while True :
            if s_idx == len(s) and p_idx == len(p) :
                return True
            if p_idx == len(p) and s_idx < len(s) :
                return False
            if p[p_idx] == '?' :
                p_idx += 1
                s_idx += 1
                continue
            print(s_idx, p_idx)
            if p[p_idx] == '*' :
                if p_idx == len(p) - 1 :
                    return True
                else :
                    if p[p_idx + 1] = "?" :
                        p_idx += 1
                    while p[p_idx+1] != s[s_idx] :
                        s_idx += 1
                        if s_idx >= len(s) :
                            s_idx = len(s) - 1 
                            break
                    p_idx += 1
                continue
            if p[p_idx] == s[s_idx] :
                p_idx += 1
                s_idx += 1
            else :
                return False

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
