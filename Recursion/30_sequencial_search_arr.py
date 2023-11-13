#Implement a recursive function for Sequential search in a sequence for array ?

arr = [3, 5, 1, 9, 7]
def finder(arr,target,left):
    if len(arr) == 0:
        return -1
    elif arr[left] == target:
        return left
    else:
        return finder(arr,target,left+1)
print(finder(arr,9,0))