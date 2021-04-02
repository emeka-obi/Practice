def prefix_summary(arr):
    sum1 = 0

    for i in range(len(arr)):
        sum1 += arr[i]
        arr[i] = sum1

    return arr




print(prefix_summary([3,2,1,5]))

