def quick_sort(arr):

    quick_sort_help(arr, 0, len(arr) -1)


def quick_sort_help(arr, first, last):
    if first < last:
        splitpoint = partition(arr, first ,last)

        quick_sort_help(arr, first, splitpoint -1)
        quick_sort_help(arr, splitpoint + 1, last)



def partition(arr, first, last):

    pivotvalue = arr[first]

    leftmark = first+ 1
    rightmark = last

    done = False

    while not done:

        while leftmark <= rightmark and arr[leftmark] <= pivotvalue:
            leftmark += 1

        while arr[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark -= 1
        if rightmark < leftmark:
            done = True
        else:
            (arr[leftmark], arr[rightmark]) = (arr[rightmark], arr[leftmark])

        
    (arr[first], arr[rightmark]) = (arr[rightmark], arr[first])
    return rightmark
