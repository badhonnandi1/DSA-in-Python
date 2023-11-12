#Implement a recursive function to find the GCD (greatest common divisor) of two numbers?
# 48 18 -> 6
def common_divisor(a,b):
    if b==0:
        return a 
    else:
        return common_divisor(b, a%b)

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
print(common_divisor(a,b))

# 48//18 = 2 48%18 = 12
# 18//12 = 1 18%12 = 6
# 12//6 = 2 12%6 = 0
# 6//0 = 0 6%0 = 6
# so the greatest common divisor is 6