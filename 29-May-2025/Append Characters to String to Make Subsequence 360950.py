# Problem: Append Characters to String to Make Subsequence - https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/description/

        m, n  = 0, 0

        while m < len(s) and n < len(t):
            if s[m] == t[n]:
                m, n = m+1, n+1
            else:
                m += 1
        return len(t)- n 
        