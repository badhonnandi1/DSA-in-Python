def string_length(mystring,left):
    if mystring == "": # base case
        return left
    else:
        return string_length(mystring[1:], left+1) #recursive call
 
mystring = input("Enter a string: ")
print(string_length(mystring,0))
