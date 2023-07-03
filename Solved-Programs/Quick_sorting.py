# a program to sort a list using quick sort algorithm
# Comparison Sorting

def quik_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        # what is pivot? pivot is the last item in the list
        pivot = arr.pop() # this line means that the last item in the list is the pivot item
    items_greater = [] # this line means that the items greater than the pivot item will be stored in this list
    items_lower = [] # this line means that the items lower than the pivot item will be stored in this list
    for item in arr:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)
    return quik_sort(items_lower) + [pivot] + quik_sort(items_greater)

# Driver code
if __name__ == '__main__':
    # input array
    arr = [1, 2, 3, 4, 3, 2, 1]
    # Calling the function
    print(quik_sort(arr))