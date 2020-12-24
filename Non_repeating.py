

def non_repeating(arr):
    for i in range(len(arr)):
        if arr[i] != arr[i+1]:
            return arr.pop(i+1)


if __name__ == "__main__":

    print(non_repeating([1,5,3,3,4,4,5,5]))



        

# def reverse_string(S):
#     for i in range(len(S)):
#         S[-1] = s[]
    