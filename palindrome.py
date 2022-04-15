def palindrome(arr):
    stack = []
    stack.extend(arr)   # 0(n)*

    count = 0
    while count < len(arr):
        count += 1
        if stack[len(arr)-count-1] == arr[len(arr)-count-1]:
           
            stack.pop()
       

    return len(stack) == 0


# This code runs through the length of the array at every call to the function. For the extend operation 0(n)* and for the while 
# loop O(n). Hence O(n)* + O(n) = O(2n) = O(n)
if __name__ == "__main__":
    print(palindrome("madam"))


