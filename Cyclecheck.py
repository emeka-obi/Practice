def cycklecheck(node):
    marker1 = node
    marker2 = node
 
# using two markers. Great interview technique

    while marker2 != None and marker2.nextnode != None:
        marker1 = marker1.nextnode
        marker2 = marker2.nextnode.nextnode

        if marker2 == marker1:
            return True 

        
    return False



