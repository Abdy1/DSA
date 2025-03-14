# Problem: Remove Comments - https://leetcode.com/problems/remove-comments/

class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        block = False
        ans = []
        current_line = []
        for line in source:
            i = 0
            n = len(line)
            while i < n:
                if block:
                    if i + 1 < n and line[i] == '*' and line[i + 1] == '/':
                        block = False
                        i += 1
                    i += 1
                else:
                    if i + 1 < n and line[i] == '/' and line[i + 1] == '*':
                        block = True
                        i+= 1
                    
                    elif i + 1 < n and line[i] == '/' and line[i + 1] == '/':
                        break
                    else:
                        current_line.append(line[i])
                    i += 1
                
            if not block and current_line:
                    ans.append("".join(current_line))
                    current_line = []
        return ans

             