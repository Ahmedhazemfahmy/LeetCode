# Given a string s containing just the characters 
# '(', ')'
# , '{', '}'
# , '[' and ']',
# determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
# Example 1:
# Input: s = "()"
# Output: true
# Example 2:
# Input: s = "()[]{}"
# Output: true
# Example 3:
# Input: s = "(]"
# Output: false
######################################################################################################################################
# string = ('(', ')', '[', ']', '{', '}')
#i= ( = 0 , ) = 1, [ = 2, ] = 3, { = 4, } = 5 


# class Valid:
#     def __inti__(self, string):
#         self.string = string

#     @classmethod
#     def brackets(cls):
#         return cls ()
    

# valid1 = Valid.brackets()
    


# string = ('(', ')', '[', ']', '{', '}')
#i= ( = 0 , ) = 1, [ = 2, ] = 3, { = 4, } = 5 

#trying Bool for some reasons..
# x = string[1] == string[2]
# y= string[1] == string[1]
# print(y)

# def valid():
#     for i in string:
#         if i != i[2]:
#             print("MIGHT WORK")

# valid()

# s1 = string[0]
# s2 = string[1]
# s3 = string[2]
# s4 = string[3]

# x = s1 + s2

# if x == ("()"):
#     print("working")

# string = ('(', ')', '[', ']', '{', '}')

# result = []

# def Valid():
    

#     for i in range(0, len(string)-1, 2):
#          result.append(string[i] + string[i+1])

# print(result)


# class Solution:
#     def is_Valid(self):
#         for i in range(0, len(self.s)-1, 2):
#             self.result.append(self.s[i] + self.s[i+1])

# # Example Usage:
# s = ['(', ')', '[', ']', '{', '}']
# pair_adder = Solution(s)
# pair_adder.is_Valid()
# print(pair_adder.result)



class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        string_dict = { ")" : "(", "]" : "[", "}" : "{" }

        for i in s:
            if i in string_dict:
                if stack and string_dict[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
                
        return True if not stack else False
