# Problem: Smallest Value of the Rearranged Number - https://leetcode.com/problems/smallest-value-of-the-rearranged-number/description/

class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0
        
        is_negative = num < 0
        digits = list(str(abs(num)))
        
        if is_negative:
            # Sort in descending order for the most negative value
            digits.sort(reverse=True)
            result = -int("".join(digits))
        else:
            # Sort in ascending order, handle leading zero case
            digits.sort()
            if digits[0] == '0':
                for i in range(1, len(digits)):
                    if digits[i] != '0':
                        # Swap first non-zero with the zero
                        digits[0], digits[i] = digits[i], digits[0]
                        break
            result = int("".join(digits))
        
        return result
