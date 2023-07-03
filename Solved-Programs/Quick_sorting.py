# # a program to sort a list using quick sort algorithm
# # Comparison Sorting

# def quik_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     else:
#         # what is pivot? pivot is the last item in the list
#         pivot = arr.pop() # this line means that the last item in the list is the pivot item
#     items_greater = [] # this line means that the items greater than the pivot item will be stored in this list
#     items_lower = [] # this line means that the items lower than the pivot item will be stored in this list
#     for item in arr:
#         if item > pivot:
#             items_greater.append(item)
#         else:
#             items_lower.append(item)
#     return quik_sort(items_lower) + [pivot] + quik_sort(items_greater)

# # Driver code
# if __name__ == '__main__':
#     # input array
#     arr = [1, 2, 3, 4, 3, 2, 1]
#     # Calling the function
#     print(quik_sort(arr))

# Given a list of integers, count and return the number of times each value appears as an array of integers.
# def count(arr):
#     # Initialize the value of result
#     result = []
#     for i in arr:
#         result.append(arr.count(i)) # this line means that the number of times each value appears in the list will be stored in the result list
#     return result


# Given a list of integers, count and return the number of times each value appears as an array of integers.
def countingSort(arr):
    # Write your code here
    result = [0] * 100 # this line means that the result list will have 100 items and each item will be 0
    for i in arr:
        result[i] += 1 #this line means that the value of result[i] will be increased by 1
    return result
