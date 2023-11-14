#Draw a lower mirror triangle pattern using recursion

def row_print(n,user):
  if n>user:
    return 
  
  else:
    def col_print(x,N):
      if x>N:
        return 
      else:
        print(x,end='')
        return col_print(x+1,N)
    def space(amount):
      if amount == 0:
        return ''
      else:
        print(end=' ')
        return space(amount-1)

    space(user-n)
    col_print(1,n)
    print()
    return row_print(n+1,user)

user = int(input("Please Enter the number: "))
assert user > 0, "Please enter a positive number"
row_print(1,user)

#     1
#    12
#   123
#  1234
# 12345