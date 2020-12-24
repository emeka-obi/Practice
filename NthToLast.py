def ntolast(head,N):
    current_node = head
    right_pointer= head
    for i in range(N-1):
        if right_pointer.nextnode == None:
            raise LookupError("Error: N is larger than the linked list")

        right_pointer = right_pointer.nextnode


    while right_pointer.nextnode:

        current_node = current_node.nextnode
        right_pointer = right_pointer.nextnode

    return current_node

    

