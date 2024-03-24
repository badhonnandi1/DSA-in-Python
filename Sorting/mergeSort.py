#created by Badhon nandi(2024)
def marge(arr,left,right,mid):# -----------------> O(nlogn) time complexity space -> O(n)
    ar1 = mid - left + 1
    ar2 = right - mid

    L = [0] * ar1
    R = [0] * ar2

    for i in range(ar1):
        L[i] = arr[left+i]

    for j in range(ar2):
        R[j] = arr[mid+j+1]

    i = 0
    j = 0
    k = left

    while i < ar1 and j < ar2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i +=1
        else:
            arr[k] = R[j]
            j +=1
        k += 1

    while i < ar1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < ar2:
        arr[k] = R[j]
        j += 1
        k += 1

def margeSort(arr,left,right):
    if left < right:
        mid = (left+right)//2
        margeSort(arr,left,mid)
        margeSort(arr,mid+1,right)
        marge(arr,left,right,mid)
    return arr


arr = [5, 9, 3, 1]
print(margeSort(arr, 0, len(arr) - 1))


# Marge Sort
    # - Marge sort is a divide and conquer algorithm
    # - Divide the input array in two halves and we keep halving recursively until they become too small that cannot be broken further
    # - Merge halves by sorting them

# When to use Marge Sort?
    # - When you need stable sort
    # - When average expected time is O(nlogn)

# When to avoid Marge Sort?
    # - When space is concern


#simulation:
#[5 , 9 , 3 , 1]
#[5 , 9] ,  [3 , 1]
#[5] , [9], [3] , [1]
#[5 , 9] , [1 , 3]
#[1 , 3 , 5 , 9]