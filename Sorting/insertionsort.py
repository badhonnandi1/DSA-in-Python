#created by Badhon nandi(2024)
def insertionSort(arr): # -----------------> O(n^2) time complexity space -> O(1)
    for i in range(len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -=1
        arr[j+1] = key

    return arr


arr = [5,9,3,1,2,8,4,7,6]
insertionSort(arr)
print(arr)

# **Insertion Sort**
    # - Divide the given array into two part
    # - Take first element from unsorted array and find its corrent position in sorted array
    # - Repeat until unsorted array is empty

# **When to use insertionSort?**
    # - When we have continous inflow of numbers and we want to keep them sorted
    # - space is a concern
    # - Easy to implement

# **When to avoid insertionSort Sort?**
    # - Average time compleixty is poor O(n^2)

#simulation:
# [5, 9, 3, 1, 2, 8, 4, 7, 6]
# [5, 9, 3, 1, 2, 8, 4, 7, 6]
# [3, 5, 9, 1, 2, 8, 4, 7, 6]
# [1, 3, 5, 9, 2, 8, 4, 7, 6]
# [1, 2, 3, 5, 9, 8, 4, 7, 6]
# [1, 2, 3, 5, 8, 9, 4, 7, 6]
# [1, 2, 3, 4, 5, 8, 9, 7, 6]
# [1, 2, 3, 4, 5, 7, 8, 9, 6]

# [1, 2, 3, 4, 5, 6, 7, 8, 9]