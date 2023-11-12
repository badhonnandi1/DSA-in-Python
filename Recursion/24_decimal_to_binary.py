#Implement a recursive function to convert decimal numbers to binary numbers.
# 13 -> 1101
def decimal_to_binaal(decimal):
    if decimal==0:
        return 0
    else:
        return decimal%2 + 10*decimal_to_binaal(decimal//2)

user = int(input("Enter a number: "))
print(decimal_to_binaal(user))

#if 13
# 13%2 = 1⭐️
# 13//2 = 6
# 6%2 = 0⭐️
# 6//2 = 3
# 3%2 = 1⭐️
# 3//2 = 1
# 1%2 = 1⭐️

# 1 + 10*0 + 100*1 + 1000*1 = 1101 -> 13
