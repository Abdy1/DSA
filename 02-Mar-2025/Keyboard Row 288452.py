# Problem: Keyboard Row - https://leetcode.com/problems/keyboard-row/description/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        ans = []
        for word in words:
            for i in range(len(word)):
                if word[i].lower() not in "qwertyuiop":
                    # print(word[i],"of ", word, "not in first")
                    break
            else:
                ans.append(word) 
            for i in range(len(word)):
                if word[i].lower() not in "asdfghjkl":
                    # print(word[i],"of ", word, "not in second")
                    break
            else:
                ans.append(word)
            for i in range(len(word)):
                if word[i].lower() not in "zxcvbnm":
                    # print(word[i],"of ", word, "not in third")
                    break
            else:
                ans.append(word) 
        return ans