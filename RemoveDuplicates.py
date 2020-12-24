def removeDuplicates(arr):
    
    N = len(arr)
    if N <=1: return N
    i = j = 1
    while i < N:
        if arr[i] != arr[i-1]:
            arr[j] = arr[i]
            j+=1
        count += 1
    return [:j]



if __name__ == "__main__":
    print(removeDuplicates([1,3,3,4,5,6,7,8,9,9,10]))