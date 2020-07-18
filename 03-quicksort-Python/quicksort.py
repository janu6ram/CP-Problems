"""Implement quick sort in Python.
Input a list.
Output a sorted list."""


def quicksort(array):
    # Your code goes here
    low = 0
    high = len(array)-1
    quickSort(array, low, high)
    return array


def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)


def partition(arr, low, high):
    i = low - 1
    pivot = high
    for j in range(low, high-1):
        if arr[j] < arr[pivot]:
            i += 1
            swap(arr, i, j)
    swap(arr, i+1, pivot)
    print(arr)
    return i+1


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


print("last", quicksort([5, 4, 8, 3, 7]))
