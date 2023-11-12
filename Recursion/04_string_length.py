def string_length(mystring,left):
    if left>=len(mystring):
        return 0 # base case
    else:
        return 1+string_length(mystring,left+1) #recursive call
 
mystring = input("Enter a string: ")
print(string_length(mystring,0))