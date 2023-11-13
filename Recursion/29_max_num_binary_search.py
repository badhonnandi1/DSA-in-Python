arr = [3, 5, 1, 10, 7, 9, 3]

def findMax(arr,low, high):
    if low == high:
        return arr[low]
    else:
        mid = (low + high)//2
        leftMax = findMax(arr,low,mid)
        rightMax = findMax(arr,mid+1,high)
        return max(leftMax,rightMax)

print(findMax(arr,0,len(arr)-1))
