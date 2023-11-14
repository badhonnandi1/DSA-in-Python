#Complete the recursive function flattenList which will take a nested python list and an empty list as parameters. The function should convert the nested list into a new flat list sequentially. 

# given_list = [1, [2, [3, [4], 5], 6], 7, 8, [9, [[10, 11], 12], 13], 14, [15, [16, [17]]]] 
# output_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17] 


given_list = [1, [2, [3, [4], 5], 6], 7, 8, [9, [[10, 11], 12], 13], 14, [15, [16, [17]]]] 
another_list = []
#using left pointer
def flattenList(given_list,another_list,left):
    if left >= len(given_list): # base case
        return
    else:
        if type(given_list[left]) == list:
            flattenList(given_list[left],another_list,0) # recursive call
        else:
            another_list.append(given_list[left]) 
        
        flattenList(given_list,another_list,left+1) # recursive call

flattenList(given_list,another_list,0)
print(another_list)

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

#using slicing
another_list = []

def flattenList(given_list,another_list):
    if len(given_list) == 0: # base case
        return 
    else:
        if type(given_list[0]) == list:
            flattenList(given_list[0],another_list) # recursive call
        else:
            another_list.append(given_list[0])
        
        flattenList(given_list[1:],another_list) # recursive call
    
flattenList(given_list,another_list)
print(another_list)
    

#using for loop
another_list = []
given_list = [1, [2, [3, [4], 5], 6], 7, 8, [9, [[10, 11], 12], 13], 14, [15, [16, [17]]]] 
def flattenList(given_list,another_list):
    for i in given_list:
        if type(i) == list:
            flattenList(i,another_list)
        else:
            another_list.append(i)
flattenList(given_list,another_list)
print(another_list)