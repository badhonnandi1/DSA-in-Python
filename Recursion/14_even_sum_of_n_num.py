#Implement a recursive function to calculate the sum of even numbers from 1 to N?
# 2 + 4 + 6 + 8 + 10 = 30

def even_sum(n):
    if n==0:
        return n
    else:
        if n%2==0:
            return n+even_sum(n-1)
        else:
            return even_sum(n-1)
        
user = int(input("Enter a number: "))
print(even_sum(user))