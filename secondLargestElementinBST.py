class Node:  
  
    # Constructor to create a new node  
    def __init__(self, data):  
        self.key = data  
        self.left = None
        self.right = None
          
# A function to find 2nd largest  
# element in a given tree.  
def secondLargestUtil(root, c): 
      
    # Base cases, the second condition  
    # is important to avoid unnecessary 
    # recursive calls  
    if root == None or c[0] >= 2:  
        return
  
    # Follow reverse inorder traversal so that  
    # the largest element is visited first  
    secondLargestUtil(root.right, c) 
  
    # Increment count of visited nodes  
    c[0] += 1
  
    # If c becomes k now, then this is 
    # the 2nd largest  
    if c[0] == 2: 
        print("2nd largest element is",  
                              root.key)  
        return
  
    # Recur for left subtree  
    secondLargestUtil(root.left, c) 