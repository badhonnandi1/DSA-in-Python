#created by Badhon nandi(2024)
def selectionSort(arr): # -----------------> O(n^2) time complexity space -> O(1)
    for i in range(len(arr)-1):
        minidx = i

        for j in range(i+1,len(arr)):
            if arr[j] < arr[minidx]:
                minidx = j

        temp = arr[i]
        arr[i] = arr[minidx]
        arr[minidx] = temp

arr = [5,9,3,1,2,8,4,7,6]
selectionSort(arr)
print(arr)


# Selection Sort
    # - In case of selection sort we repeatedly find the minimum element and move it to the sorted part of array to make unsorted part sorted


# **When to use Bubble Sort?**
    # - space is a concern
    # - Easy to implement

# **When to avoid Bubble Sort?**
    # - Average time compleixty is poor O(n^2)

#simulations:
# [5, 9, 3, 1, 2, 8, 4, 7, 6]
# [1, 9, 3, 5, 2, 8, 4, 7, 6]
# [1, 2, 3, 5, 9, 8, 4, 7, 6]
# [1, 2, 3, 5, 9, 8, 4, 7, 6]
# [1, 2, 3, 4, 9, 8, 5, 7, 6]
# [1, 2, 3, 4, 5, 8, 9, 7, 6]
# [1, 2, 3, 4, 5, 6, 9, 7, 8]
# [1, 2, 3, 4, 5, 6, 7, 9, 8]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]