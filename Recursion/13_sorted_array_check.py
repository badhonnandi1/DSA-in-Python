#Write a recursive function to check if an array is sorted in assending order.

arr = [1,2,3,4,5,6,7]
def assendingsorted(arr,left):
    if left == len(arr)-1:
        return True # Base case
    elif arr[left] > arr[left+1]:
        return False # Base case
    else:
        return assendingsorted(arr,left+1) # Recursive case

#Write a recursive function to check if an array is sorted in desending order.

def desendingsorted(arr,left):
    if left == len(arr)-1:
        return True # Base case
    elif arr[left] < arr[left+1]:
        return False # Base case
    else:
        return desendingsorted(arr,left+1) # Recursive case


print(assendingsorted(arr,0)) # True
print(desendingsorted(arr,0)) # False