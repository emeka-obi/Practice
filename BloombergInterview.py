def moveZeros(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1

    while count < N:
        arr[count] = 0

    return arr



def flattenLinkedList(head):
    curr = head
    while curr:
        temp = curr:
        while temp.down:
            temp = temp.down
        temp.down = curr.next
        curr = curr.next

def 

if __name__ == "__main__":


    