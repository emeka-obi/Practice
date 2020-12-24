def seq_search(arr,ele):
    count = 0
    isFound = False
    while count <= len(arr)-1 and isFound != True:
        if arr[count] == ele:
            isFound = True
            return isFound
        
        count += 1
            
    return -1
"""Input array should be ordered"""
def seq_ordered_search(arr,ele):
 
    for i in arr:
        if i > ele:
            break
        elif i == ele:
            return i

if __name__ == "__main__":
    print(seq_search([2,6,7,9],10))