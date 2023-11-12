#Write a recursive function to find the nth term of the Lucas sequence (similar to Fibonacci)?
# 2,1,3,4,7,11,18,29,47,76..

def lucas_sequesnce(n):
    if n==0:
        return 2
    elif n==1:
        return 1
    else:
        return lucas_sequesnce(n-1)+lucas_sequesnce(n-2)

user = int(input("Enter a number: "))
print(lucas_sequesnce(user))
