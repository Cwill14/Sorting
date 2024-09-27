# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr)):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # loop through right side of 
        for j in range(cur_index + 1, len(arr)):
            # find smallest element
            if arr[j] < arr[smallest_index]:
                smallest_index = j
            # TO-DO: swap
            print(f"arr: {arr}")
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
        
    return arr

# a = [2, 9, 4, 6, 45, 1, 5, 3, 7, 8, 0, 10, 75]
# print(selection_sort(a))

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    # BELOW IS A LIE   
    swapped = True
    # LIE ^^^^^^^^
    # if no swaps performed, stop. else, go back to element at index 0 and repeat step 1
    while swapped == True:
    # loop through array
        swapped = False
        for i in range(1, len(arr)):
        #     # compare to neighbor
            if arr[i] < arr[i - 1]:
        #         # if elements in wrong position (relative to each other), swap
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                swapped = True

    return arr

#    0  1  2  3  4   5  6  7  8  9  10 11  12
a = [75, 2, 9, 4, 6, 45, 1, 5, 3, 7, 8, 0, 10, 14]
print(bubble_sort(a))

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr