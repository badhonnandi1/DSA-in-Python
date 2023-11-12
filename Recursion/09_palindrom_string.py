#Implement a recursive function to check if a string is a palindrome.
# "ABCCBA" -> True
def is_palindrome(mystring):
    if len(mystring) <= 1:
        return True
    else:
        if mystring[0] == mystring[len(mystring)-1]:
            return is_palindrome(mystring[1:len(mystring)-1])
        else:
            return False

mystring = input("Enter a string: ")
if is_palindrome(mystring):
    print("Palindrome")
else:
    print("Not palindrome")

# ABCCBA
# BCCB
# CC
# Palindrome
