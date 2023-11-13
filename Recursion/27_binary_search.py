#Implement Binary Search using recursion?
#Binary Search: Search a sorted array by repeatedly dividing the search interval in half. Begin with an interval covering the whole array. If the value of the search key is less than the item in the middle of the interval, narrow the interval to the lower half. Otherwise, narrow it to the upper half. Repeatedly check until the value is found or the interval is empty.
#The idea of binary search is to use the information that the array is sorted and reduce the time complexity to O(Log n).
x = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
def binary_search(x,target,low,high):
    if low > high:
        return -1
    else:
        mid = (low+high)//2

        if x[mid] == target:
            return mid
        elif x[mid] < target:
            return binary_search(x,target, mid + 1, high);
        else:             
            return binary_search(x,target, low , mid - 1);

print(binary_search(x,7,0,len(x)-1))


#We basically ignore half of the elements just after one comparison.


# iterative approach
# ->
# def binary_search(x,target):
#     low = 0
#     high = len(x)-1

#     while low<=high:
#         mid = (low+high)//2

#         if x[mid] == target:
#             return mid
#         elif x[mid] < target:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return -1

# print(binary_search(x,7))
