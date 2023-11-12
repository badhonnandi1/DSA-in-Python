#Write a recursive function to count the number of digits in a positive integer.
# 1234 = 4

def digit_count(n):
    if n == 0:
        return 0    # Base case
    else:
        return 1+digit_count(n//10) # Recursive case

user = int(input("Enter a number: ")) 
print(digit_count(user))