def binary_search(arr,ele):
    first = 0
    last = len(arr) -1
    found = False
    
    while first <= last and found != True:
        mid = (first + last)//2
        print(mid)

        if arr[mid] == ele:
            found = True

        else:
            if ele < arr[mid]:
                last = mid - 1

            else:
                first = mid + 1
    return found 





# def recursive_binary_search(arr,ele):
#       if  len(arr) == 0:
#           return False
#       else:
#           mid = (len(arr)-1)//2
          
#           if arr[mid] == ele:
#               return True

#           else:
#                 if ele < arr[mid]:
#                     return recursive_binary_search(arr[ :mid],ele)

#                 else:
#                     return recursive_binary_search(arr[mid+1],ele)

if __name__ == "__main__":
    print(binary_search([2,4,7,8,9,12,14,17,19,22,25,27,28,33,37],4))
