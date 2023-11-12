#Write a recursive function to find the sum of the first N natural numbers?
# 1+2+3+4+5+6+7+8+9+10 = 55
def sum_finder(n):
    if n==0:
        return 0 # 0! = 1! = 1 base case
    else:
        return n+sum_finder(n-1) # 5+4+3+2+1
    

user = int(input("Enter a number: "))
print(sum_finder(user)) 

