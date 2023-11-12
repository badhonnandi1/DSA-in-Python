#Implement a recursive function to find the maximum element in an array?
# [3,4,2,5,7,4,3,5] -> 7

arr = [3,4,2,5,7,4,3,5]
def max_value(arr,left):
    if left == len(arr) - 1:
        return arr[left] # base case
    else:
        return max(arr[left],max_value(arr,left+1))
    
print(max_value(arr,0))