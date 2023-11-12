def string_digit_sum(string):
    if len(string)==0: # base case
        return 0
    else:
        return int(string[0]) + string_digit_sum(string[1:]) # recursive case
    
string = input("Enter a string: ")
print(string_digit_sum(string))
