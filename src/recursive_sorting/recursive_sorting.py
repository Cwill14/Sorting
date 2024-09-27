# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    merged_arr = []

    while len(arrA) != 0 and len(arrB) != 0:
        if arrA[0] < arrB[0]:
            merged_arr.append(arrA[0])
            arrA.remove(arrA[0])
        else:
            merged_arr.append(arrB[0])
            arrB.remove(arrB[0])

    if len(arrA) == 0 and len(arrB) != 0:
        # for i in arrB:
        for i in range(0, len(arrB)):
            merged_arr.append(arrB[i])
    else:
        # for i in arrA:
        for i in range(0, len(arrA)):

            merged_arr.append(arrA[i])

    return merged_arr

# s1 = [1, 2, 3, 4]
# s2 = [5, 6, 7, 8, 9]
# print(merge(s1, s2))

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

print(merge_sort([2, 4, 5, 10, 6, 1, 3, 7]))

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
