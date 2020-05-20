# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    current_index_arrA = 0
    current_index_arrB = 0
    current_index_merged = 0
    while current_index_merged < elements:
        is_arrB_exhausted = current_index_arrB >= len(arrB)
        is_arrA_exhausted = current_index_arrA >= len(arrA)
        if (not is_arrB_exhausted and (is_arrA_exhausted or arrB[current_index_arrB] < arrA[current_index_arrA])):
            merged_arr[current_index_merged] = arrB[current_index_arrB]
            current_index_arrB += 1
        else:
            merged_arr[current_index_merged] = arrA[current_index_arrA]
            current_index_arrA += 1
        current_index_merged += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Your code here
    if len(arr) > 1:
        left = merge_sort(arr[:len(arr) // 2])
        right = merge_sort(arr[len(arr) // 2:])
        arr = merge(left, right)

    return arr


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here
    start2 = mid + 1
    if arr[mid] <= arr[start2]:
        return
    while start <= mid and start2 <= end:
        if arr[start] <= arr[start2]:
            start += 1
        else:
            value = arr[start2]
            index = start2
            while index != start:
                arr[index] = arr[index - 1]
                index -= 1
            arr[start] = value
            start += 1
            mid += 1
            start2 += 1


def merge_sort_in_place(arr, l, r):
    # Your code here
    if l < r:
        m = 1 + (r -1) // 2
        merge_sort_in_place(arr, l, m)
        merge_sort_in_place(arr, m + 1, r)
        merge_in_place(arr, l, m, r)


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
