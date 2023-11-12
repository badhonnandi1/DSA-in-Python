#Write a recursive function to compute the product of two numbers without using the multiplication operator.
# 5*3 = 5+5+5 = 15
def two_number_product(a,b):
    if b==0:
        return 0
    else:
        return a+two_number_product(a,b-1)

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print(two_number_product(a,b))