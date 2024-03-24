#created by Badhon nandi(2024)
def swap(mylist,idx1,idx2):
    temp = mylist[idx1]
    mylist[idx1] = mylist[idx2]
    mylist[idx2] = temp

def pivot(mylist,pivotidx,endidx):
    swapidx = pivotidx
    for i in range(pivotidx+1,endidx+1):
        if mylist[i] < mylist[pivotidx]:
            print(mylist)
            swapidx += 1
            swap(mylist,swapidx,i)
            print(mylist)
    swap(mylist,pivotidx,swapidx)
    return swapidx

def quickSort(mylist,left,right):
    if left < right:
        pivetidx = pivot(mylist,left,right)
        quickSort(mylist,left,pivetidx-1)
        quickSort(mylist,pivetidx+1,right)
    return mylist

mylist = [3,5,0,6,2,1,4]
quickSort(mylist,0,len(mylist)-1)
print(mylist)

# Quick Sort:
    # Quick sort is a divide and conquer algorithm.
    # It works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays according to whether they are less than or greater than the pivot.
    # The sub-arrays are then recursively sorted.

# When to use Quick Sort?
    # When you need an efficient sorting algorithm with an average expected time complexity of O(nlogn).
    # It's suitable for large datasets.
    # Quick sort is also an in-place sorting algorithm, meaning it doesn't require additional memory beyond the array being sorted.

# When to avoid Quick Sort?
    # Quick sort can exhibit poor performance on already sorted arrays or arrays with many duplicate elements. In such cases, it may perform closer to O(n^2) time complexity.
    # It's not stable; that is, the relative order of equal elements may change after sorting.
    # When stability in sorting is required, other algorithms like Merge Sort or Tim Sort might be preferred.

#simulation:
# [3, 5, 0, 6, 2, 1, 4]
# [3, 5, 0, 6, 2, 1, 4]
# [3, 0, 5, 6, 2, 1, 4]
# [3, 0, 5, 6, 2, 1, 4]
# [3, 0, 2, 6, 5, 1, 4]
# [3, 0, 2, 6, 5, 1, 4]
# [3, 0, 2, 1, 5, 6, 4]
# [1, 0, 2, 3, 5, 6, 4]
# [1, 0, 2, 3, 5, 6, 4]
# [1, 0, 2, 3, 5, 6, 4]
# [0, 1, 2, 3, 5, 6, 4]
# [0, 1, 2, 3, 5, 6, 4]
# [0, 1, 2, 3, 5, 4, 6]
# [0, 1, 2, 3, 4, 5, 6]