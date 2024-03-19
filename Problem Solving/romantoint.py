# we need to change the roman letters to integers
#  reference:Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

# thinking

# roman_list = {
    
#     'I' : 1,
#     'V' : 5,
#     'X' : 10,
#     'L' : 50,
#     'C' : 100,
#     'D' : 500,
#     'M' : 1000
# }

# class RomantoInteger:
#         def __init__(self, roman, intt):
#             self.roman = roman,
#             self.intt = intt


#         def convert(self):
#             pass


#thinking #2
# create Class
# input is String
# output is integer
# Create a list of roman = to the meaning in integer (key:value)
#loop by checking if len S is smaller than the equivelent in the roman list, and if the roman number is less than the other roman number
# I is less than V so IV = 4 and not written as VI..V = 5 and IV meaning is 4 5 = 5-4 = 1 in roman way so we have to substract
class Soluting:
    def romanToInt(self, s:str) -> int:
        roman_list = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000}
        
        result = 0

        for i in range(len(s)):
            if i + 1 < len(s) and roman_list[s[i]] < roman_list[s[i +1]]:
                result -= roman_list[s[i]]
            else:
                result += roman_list[s[i]]
        return result


