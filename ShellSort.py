"The shell sort improves on the insertion sort by breaking the original list into sublists, and using an increment i to create a sublist off all items that are i letters apart"
def shell_sort(arr):
    sublistcount = len(arr)/2

    while sublistcount > 0:
        for start in range(sublistcount):

            gap_insetion_sort(arr,start,sublistcount)

        sublistcount = sublistcount/2

def gap_insetion_sort(arr,start,gap):

    for i in range(start+gap, len(arr), gap):

        currentvalue = arr[i]
        position = i

        while position >= gap and arr[position - gap]  > currentvalue:
            arr[position] = arr[position - gap]

            position = position - gap
        
        arr[position] = currentvalue
