# Problem: Integer to Roman - https://leetcode.com/problems/integer-to-roman/description/

class Solution:
    def intToRoman(self, num: int) -> str:
        changer = {1:'I',5:'V', 10:'X',50:'L',100:'C',500:'D',1000:'M'}
        skip4 = {1:'IV', 10:'XL', 100:'CD'}
        skip9 = {1:'IX', 10:'XC', 100:'CM'}
        house = 1
        answer = ''
        while num:
            number = num % 10
            if number < 4:
                for i in range(number):
                    answer = changer[house] + answer
            elif number == 4:
                answer = skip4[house] + answer
            elif number == 9:
                answer = skip9[house] + answer
            else:
                temp = changer[house * 5]
                for i in range(number - 5):
                    temp += changer[house] 
                answer = temp + answer
            house *= 10
            num //=10
        return answer
           