




def prefixaverage(arr):
    new_list = []

    sum1 = 0

    for i in range(1, len(arr)+1):
        sum1 += arr[i-1]
        prefix_average = round(sum1/i,2)
        new_list.append(prefix_average)


    return new_list



if __name__ == "__main__":

    print(prefixaverage([3,9,2,4,7]))







    