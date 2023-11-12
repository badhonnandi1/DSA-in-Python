#Write a recursive function to find if a number is a perfect number or not?

def perfect(n,divisor=1):
    if n==divisor:
        return 0 # Base case
    else:
        if n%divisor==0:
            return divisor+perfect(n,divisor+1) # Recursive case
        else:
            return perfect(n,divisor+1) # Recursive case

user = int(input("Enter a number: "))

if perfect(user)==user:
    print("Perfect number")
else:
    print("Not a perfect number")
# 6 = 1+2+3 = 6