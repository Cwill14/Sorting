# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    # elements = len( arrA ) + len( arrB )
    # merged_arr = [0] * elements
    # TO-DO
    # declare empty array. this will be end result
    
    # iterate through length of both arrays combined:
    # # also iterate through both arrays separately?
    # length = len(arrA) + len(arrB)
    # # m_arr_length = len(merged_arr)
    # print(length)
    # # while length is greater than 0? have to change length?
    # # while length < 0:
    # # while length < 0:    
    # for i in range(0, len(arrA)):
        
    #     # print(f"i: {i}")    
    #     # print(f"arrA[i]: {arrA[i]}") 

    #     return arrA[i]
    # for i in range(0, len(arrB)):
        

    #     # print(f"i: {i}")    
    #     # print(f"arrB[i]: {arrB[i]}") 
        # compare first arrA index againset first arrB index
        # smallest arrA added to merge_arr
        # increase index to next arr 
        # arrB index would have to stay the same.
        # compaare new arrA index with same arrB index

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
    # chop in 2
    # until size/lenth == 1
    # then call merge for each pair?
        # first 2 arrays, repeat
            #if only 1 array, how to pair with next array?
    # call merge again until 1 array
    return arr


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
