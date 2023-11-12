#Write a recursive function to find if a number is a prime number or not.
# 29 -> True
def primeChecker(n,divisor):
    if n==2:
        return True
    elif n<2:
        return False
    elif n%divisor==0:
        return False
    elif divisor*divisor > n:
        return True
    else:
        return primeChecker(n,divisor+1)

user = int(input("Enter a number: "))
print(primeChecker(user,2))

#The purpose of if divisor * divisor > n: return True is to stop the recursion once the divisor becomes larger than the square root of the number being checked. If we've checked all divisors up to the square root of n and haven't found a divisor, we won't find any divisors beyond that point.

# Suppose we're checking if 29 is prime. The square root of 29 is approximately 5.4. So, we only need to check divisibility by 2, 3, 4, and 5. Once we've checked those and found no divisors, we can be confident that 29 is prime.

