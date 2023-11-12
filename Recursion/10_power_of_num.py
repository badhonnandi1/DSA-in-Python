#Write a recursive function to compute the power of a number (a^b)?
# 2^3 = 2*2*2 = 8
# -2^3 = -2*-2*-2 = -8
# 2^-3 = 1/2^3 = 1/8 = 0.125
# -2^-3 = 1/-2^3 = -1/8 = -0.125
# 2^0 = 1
def power(a,b):
    if b==0: 
        return 1 # base case
    elif b<0:
        return (1/a) * power(a,b+1)
    else:
        if a<0:
            if b%2==0:
                return a * power(a,b-1)
            else:
                return abs(a) * power(a,b-1)
        else:
            return a * power(a,b-1)

a = int(input("Enter a number: "))
b = int(input("Enter a power: "))
print(power(a,b)) 