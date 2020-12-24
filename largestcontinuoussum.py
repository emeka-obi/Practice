def largest_continous_sum(Arr):
    if len(Arr) == 0:
        return 0

    current_sum = max_sum = Arr[0]

    for i in Arr[1:]:

        current_sum = max(current_sum+ i, i)

        max_sum = max(current_sum, max_sum)
        
    return max_sum



print(largest_continous_sum([1,2,-1,2,34]))