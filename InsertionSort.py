"""Much less efficient on large lists such as heap sort, insertion sort and merge sort"""

def insertion_sort(arr):
    for i in range(1, len(arr)):

        currentvalue = arr[i]
        position = i

        while position > 0 and arr[position-i] > currentvalue:
            arr[position] = arr[position-1]

            position = position -1
        
        arr[position] = currentvalue

