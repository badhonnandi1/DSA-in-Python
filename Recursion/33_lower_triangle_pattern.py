#Draw a lower triangle pattern using recursion

def row_print(n,user):
  if n>user:
    return 
  
  else:
    def col_print(x,N):
      if x>N:
        return 
        
      else:
        print(x,end=' ')
        return col_print(x+1,N)

    col_print(1,n)
    print()
    return row_print(n+1,user)

user = int(input("Please Enter the number: "))
assert user > 0, "Please enter a positive number"
row_print(1,user)

# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5 