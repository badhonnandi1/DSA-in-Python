#Implement a recursive function to reverse a string.
# "hello" -> "olleh"
def reverse_string(mystring,left):
    if left>=len(mystring):
        return "" # base case
    else:
        return reverse_string(mystring,left+1)+mystring[left] 
        #recursive call

mystring = input("Enter a string: ")
print(reverse_string(mystring,0))