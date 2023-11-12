#Write a recursive function to calculate the factorial of a number?
# 5! = 5*4*3*2*1 = 120

def factorial(n):
    if n==0 or n==1:
        return 1  # 0! = 1! = 1 base case
    else:
        return n*factorial(n-1) # 5*4*3*2*1
    
user = int(input("Enter a number: "))
print(factorial(user)) 