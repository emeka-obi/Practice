def node(head):
  current = head
  prev = None
  nextnode = None

  while current:
      nextnode = current.nextnode
      current.nextnode = prev

      prev = current

      current = nextnode

  head = prev


     