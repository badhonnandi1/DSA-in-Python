#Write a recursive function to find the LCM (least common multiple) of two numbers.
# 48 18 -> 144
# formula for least common multiple is: a*b/gcd(a,b)
# from _11_greatest_common_divisor import common_divisor

def common_divisor(a,b):
    if b==0:
        return a 
    else:
        return common_divisor(b, a%b)

def lcm(a,b):
    if a==0 or b==0:
        return 0
    else:
        return abs(a*b)//common_divisor(a,b)
    
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
print(lcm(a,b))