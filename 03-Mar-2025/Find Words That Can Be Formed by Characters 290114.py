# Problem: Find Words That Can Be Formed by Characters - https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
            chars_count = Counter(chars)
            total_length = 0

            for word in words:
                 word_count = Counter(word)
                 # Check if all characters in word can be formed using chars
                 if all(word_count[c] <= chars_count[c] for c in word_count):
                    total_length += len(word)
    
            return total_length
        