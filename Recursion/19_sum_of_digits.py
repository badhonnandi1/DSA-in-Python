#Implement a recursive function to calculate the sum of the digits of a positive integer.
# 1234 = 1+2+3+4 = 10

def sum_of_digit(n):
    if n==0:
        return 0
    else:
        return n%10 + sum_of_digit(n//10)

user = int(input("Enter a number: "))
print(sum_of_digit(user))
