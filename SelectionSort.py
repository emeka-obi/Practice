"makes only one exchnange and puts the largest element at the end of array and so on"

def Selection_sort(arr):
    for i in range(len(arr)-1,0,-1):
        positionofmax = 0

        for location in range(1, i+1):
            if arr[location] > arr[positionofmax]:
                positionofmax = location

        (arr[i], arr[positionofmax]) = (arr[positionofmax], arr[i])
    