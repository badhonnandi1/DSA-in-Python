#Write a recursive function to print the first N natural numbers in reverse order.
# 10 9 8 7 6 5 4 3 2 1
def reverse_natural_num(n):
    if n==0:
        return 1
    elif n<0:
        print(n,end=' ')
        reverse_natural_num(n+1)
    else:
        print(n,end=' ')
        reverse_natural_num(n-1)
        

user = int(input("Enter a number: "))
reverse_natural_num(user)