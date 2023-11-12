#Implement a recursive function to calculate the nth Fibonacci number?
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 ...

def fibonacci(n):
    if n < 0:
        raise ValueError("Input must be non-negative")
    elif n == 0:
        return 0 # base case
    elif n == 1:
        return 1 # base case
    else:
        return fibonacci(n-1) + fibonacci(n-2) # recursive call
    
user = int(input("Enter a number: "))
print(fibonacci(user)) 

      



