def Bubble_sort(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                (arr[j], arr[j+1]) = (arr[j+1], arr[j])
    return arr
        
        

if __name__ == "__main__":
    print(Bubble_sort([9,9,21,5,6,1]))
# for i in range(len(arr)-1,0,-1):
#     for k i range(i):
#         print(i)
