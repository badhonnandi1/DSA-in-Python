#Write a recursive function to find the minimum element in an array?
# [3,4,2,5,7,4,3,5] -> 2

arr = [3,4,2,5,7,4,3,5]
def min_value(arr, left):
    if left == len(arr) - 1:
        return arr[left] # base case
    else:
        return min(arr[left], min_value(arr, left + 1)) #recursive call

print(min_value(arr, 0))
