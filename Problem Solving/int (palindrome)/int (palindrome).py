#palindrome meaning is the number that's equal to the reversed number. 
#example givin: 121 

x = 131
#switch to string 
s = str(x)
reversed_str = str(x)[::-1]
def palindrome(x): 
    if x < 0:
        return False
    elif str(x) == reversed_str:
        return True
    else:
        return False

number = 131
result = palindrome(number)

print(f"is {number} a palindorme? {result}")