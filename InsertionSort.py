"""Much less efficient on large lists such as heap sort, insertion sort and merge sort"""


def insertion_sort(A):
    for k in range(1, len(A)):
        cur = A[k]
        j = k
        while j >0 and A[j-1] > cur:
            A[j] = A[j-1]
            j -= 1
            A[j] = cur

        print(A)




print(insertion_sort([6,8,2,3,9,4,7,1]))