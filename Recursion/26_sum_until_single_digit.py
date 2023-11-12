
def sum_of_digit(n):
    if n==0:
        return 0
    else:
        return n%10 + sum_of_digit(n//10)

def single_digit_sum(n):
    if n<10:
        return n
    else:
        digit_sum = sum_of_digit(n)
        return single_digit_sum(digit_sum)

user = int(input("Enter a number: "))
print(single_digit_sum(user))

# 