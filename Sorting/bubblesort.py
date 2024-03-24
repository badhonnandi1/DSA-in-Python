#created by Badhon nandi(2024)
def bubblesort(arr):# -----------------> O(n^2) time complexity space -> O(1)
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
arr = [5,9,3,1,2,8,4,7,6]
bubblesort(arr)
print(arr)

# Bubble Sort
    #  - Bubble sort is also referred as sinking sort
    #  - we repeatedly compare each pair of adjacnt items and swap them if they are in the wrong order

#When to use Bubble Sort?

    # - When the input is already sorted
    # - space is a concern
    # - Easy to implement

# **When to avoid Bubble Sort?**
    # - Average time compleixty is poor O(n^2)

# Simulation step by step:
# [5, 9, 3, 1, 2, 8, 4, 7, 6]
# [5, 9, 3, 1, 2, 8, 4, 7, 6]
# [5, 3, 9, 1, 2, 8, 4, 7, 6]
# [5, 3, 1, 9, 2, 8, 4, 7, 6]
# [5, 3, 1, 2, 9, 8, 4, 7, 6]
# [5, 3, 1, 2, 8, 9, 4, 7, 6]
# [5, 3, 1, 2, 8, 4, 9, 7, 6]
# [5, 3, 1, 2, 8, 4, 7, 9, 6]
# [5, 3, 1, 2, 8, 4, 7, 6, 9]
# [3, 5, 1, 2, 8, 4, 7, 6, 9]
# [3, 1, 5, 2, 8, 4, 7, 6, 9]
# [3, 1, 2, 5, 8, 4, 7, 6, 9]
# [3, 1, 2, 5, 8, 4, 7, 6, 9]
# [3, 1, 2, 5, 4, 8, 7, 6, 9]
# [3, 1, 2, 5, 4, 7, 8, 6, 9]
# [3, 1, 2, 5, 4, 7, 6, 8, 9]
# [1, 3, 2, 5, 4, 7, 6, 8, 9]
# [1, 2, 3, 5, 4, 7, 6, 8, 9]
# [1, 2, 3, 5, 4, 7, 6, 8, 9]
# [1, 2, 3, 4, 5, 7, 6, 8, 9]
# [1, 2, 3, 4, 5, 7, 6, 8, 9]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]