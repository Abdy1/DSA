# Problem: Find Common Characters - https://leetcode.com/problems/find-common-characters/

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ans = []
        not_everywhere = False
        for char in words[0]:
            not_everywhere = False
            for i in range(1,len(words)):
                if char not in words[i]:
                    not_everywhere = True
                else:
                    print(words[i])
                    words[i] = list(words[i])
                    words[i].remove(char)
                    words[i] = "".join(words[i])
           
                    print(words[i])
            if not not_everywhere:
                ans.append(char)

        return ans

        