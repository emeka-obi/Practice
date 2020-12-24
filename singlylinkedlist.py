class Node():
    def __init__(self, value):
        self.value = value
        self.nextnode = None

    def show(self, head):
        while head:
            head = head.nextvalue
            print(head.value)

a = Node(1) 
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)
g = Node(7)
h = Node(8)



a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e
e.nextnode = f
f.nextnode = g
g.nextnode = h
# print(a.value)
# print(a.nextnode.value)
# dummy node comes to play when you need to remove a node in the fist and last index

"""access an element in a linked list"""


def del_m_nodes_after_n(head, m, n):

    current1 = head
    current2 = head

    while current1.next:
        
        current1 = current1.nextnode
        
def searchlist(a,n):
    current = a
    count = 0

    for i in range(n-1):
        count += 1
        current = current.nextnode
    
    return current.value, count


def NthTolast(head, n):
    marker1 = head
    marker2 = head

    for i in range(n-1):
        if marker2.nextnode == None:
            raise LookupError("No element at this position")
        marker2 = marker2.nextnode
    
    while marker2.nextnode:

        marker2 = marker2.nextnode
        marker1 = marker1.nextnode
    
    return marker1.value


def lengthofelement(head):

    count = 0
    current = head
    while current:
        count +=1
        current = current.nextnode
    return count

def reverseLinkedList(head):
    
    current = head
    prev = None
    nextnode = None

    while current:

        nextnode = current.nextnode
        current.nextnode = prev
        prev = current
        current = nextnode

    return prev.value


def cycleCheck(head):

    marker1 = head
    marker2 = head

    while marker2.nextnode:
        marker2 = marker2.nextnode.nextnode
        marker1 = marker1.nextnode

        if marker2 == marker1:

            return True

    return False


def del_node(head, data):
    #if the node to delete  is at the head
  
    curr = head

    if curr and curr.value == data:
        head = curr.nextnode
        curr = None

    #if the node to delete is anywhere else
    prev = None
    while curr and curr.value != data:
        prev = curr
        curr = curr.nextnode

    if curr is None:
        return None

    prev.next = curr.nextnode
    curr = None

def del_node_at_position(head,n):
    curr = head
    prev = None
  # if n is 0    
    if n == 0:
        head = curr.nextnode
        curr = None

# you could also use while curr
    for i in range(n-1):
        if curr.nextnode == None:
            raise LookupError("Position is higher than the number of elements in the linked List")
        prev = curr 
        curr = curr.next

    prev.next = curr.next
    curr = None
    

def insert_at_positon(head,data,n):
    curr = head
    new_node = Node(data)
    for i in range(n-1):
        curr = curr.next


    new_node.next = curr.next
    curr.next = new_node
    return head
    












if __name__ == "__main__":
    print(del_m_nodes_after_n(a, 1, 1))

 