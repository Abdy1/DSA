# Problem: Masking Personal Information - https://leetcode.com/problems/masking-personal-information/description/?envType=problem-list-v2&envId=string

class Solution:
    def maskPII(self, s: str) -> str:
        if "@" in s:
            s = s.lower()
            index_ = s.index("@")
            return list(s)[0]+"".join(["*"] * 5)+ s[index_-1:]
        else:
            digits = ''.join([ch for ch in s if ch.isdigit()]) 
            if len(digits) == 10:
                return "***-***-" + digits[-4:]
            
            country_code = len(digits) - 10
            masked_number = '+' + '*' * country_code + '-***-***-' + digits[-4:]
            
            return masked_number