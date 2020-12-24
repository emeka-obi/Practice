def palindrome(arr):
    stack = []
    for i in arr:
        stack.append(i)

    count = 0
    while count < len(arr):
        count += 1
        if stack[len(arr)-count-1] == arr[len(arr)-count-1]:
            stack.pop()

    return len(stack) == 0



if __name__ == "__main__":
    print(palindrome("madam"))