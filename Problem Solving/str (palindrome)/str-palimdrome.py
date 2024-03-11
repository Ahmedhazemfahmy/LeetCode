# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing
# all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.


#re is a method to remove all non-alphanumeric chars and qutatoions..
# import re


# s = ("A man, a plan, a canal: Panama")

# x = re.sub(r'[^a-zA-Z0-9]', '', s)


# s_reverse = x[::-1]

# # print(x, s_reverse)


# def palindrome(s):
#     if s == s_reverse:
#         return True
#     else:
#         return False
    
# def __str__(s):
#     return 


# string=("A man, a plan, a canal: Panama")
# palindrome(s)
# print(f" the string {string} is a palindrome {palindrome}")

# import re



# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         validation = []
#         s = ("A man, a plan, a canal: Panama")
#         cleaned = re.sub(r'[^a-zA-Z0-9]', '', s)
#         reverse = cleaned[::-1]
#         if cleaned == reverse[::-1]:
#             return True
#         else:
#             return False


# string=("A man, a plan, a canal: Panama")
# valid = Solution.isPalindrome(string)
# print(valid)



import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = re.sub(r'[^a-zA-Z0-9]', '', s.lower())  # Ignore case and remove non-alphanumeric characters
        return cleaned == cleaned[::-1]

# Example usage:
string = "A man, a plan, a canal: Panama"
sol = Solution()
valid = sol.isPalindrome(string)
print(valid)