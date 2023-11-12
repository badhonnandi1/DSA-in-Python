#Write a recursive function to calculate the sum of all elements in an array?

arr = [1,2,3,4,5] #for 1D array
def element_sum(arr,left):
    if left>=len(arr):
        return 0 # base case
    else:
        return element_sum(arr,left+1)+arr[left]   #recursive call
    
print(element_sum(arr,0))