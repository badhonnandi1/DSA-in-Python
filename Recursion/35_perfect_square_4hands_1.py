import numpy as np
myarray = np.zeros((8,8),dtype=int)
myarray[0][1] = 1
myarray[1][0] = 1
myarray[1][1] = 1
myarray[1][2] = 1
myarray[1][5] = 1
myarray[2][1] = 1
myarray[2][4] = 1
myarray[2][5] = 1
myarray[2][6] = 1
myarray[2][7] = 1
myarray[3][2] = 1
myarray[3][5] = 1
myarray[4][2] = 1
myarray[5][0] = 1
myarray[5][0] = 1
myarray[5][1] = 1
myarray[5][2] = 1
myarray[5][3] = 1
myarray[5][4] = 1
myarray[5][6] = 1
myarray[5][7] = 1
myarray[6][2] = 1
myarray[6][6] = 1
myarray[6][7] = 1
myarray[7][2] = 1
def row(myarray,r,count):
  if r<0:
    return None 
  else:
    def col(myarray,c,r1,count):
      if c<0:
        return None 
      else:
        def upper(row,col,status):
          if row<0:
            return 0
          elif myarray[row][col] == 0:
            return upper(row-1,col,False)
          else:
            if myarray[row][col] == 1 and status:
              return 1 + upper(row-1,col,status)
            else:
                  return 0

        def lower(row,col,status):
          if row>7:
            return 0
          elif myarray[row][col] == 0:
            return lower(row+1,col,False)
          else:
            if myarray[row][col] == 1 and status:
              return 1 + lower(row+1,col,status)
            else:
              return 0

        def right(row,col,status):
          if col>7:
            return 0
          elif myarray[row][col] == 0:
            return right(row,col+1,False)
          else:
            if myarray[row][col] == 1 and status:
              return 1 + right(row,col+1,status)
            else:
              return 0

        def left(row,col,status):
          if col<0:
            return 0
          elif myarray[row][col] == 0:
            return left(row,col-1,False)
          else:
            if myarray[row][col] == 1 and status:
              return 1 + left(row,col-1,status)
            else:
              return 0

        if myarray[r1][c] == 1:
          upp = upper(r1-1,c,True)
          lower = lower(r1+1,c,True)
          left = left(r1,c-1,True)
          right = right(r1,c+1,True)

          if upp == lower == left == right:
            count[0] +=1 
        col(myarray,c-1,r1,count)
    col(myarray,7,r,count)
    row(myarray,r-1,count)
count = [0]
row(myarray,7,count)
print(count[0])

print(myarray)
