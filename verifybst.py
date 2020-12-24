'''Is every node value in the root’s left subtree less than the root’s value?
Is every node value in the root’s right subtree greater than the root’s value?
Is the root’s left subtree also a binary search tree?
Is the root’s right subtree also of a binary search tree?'''


def isValidBST(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    # stack, inorder = [], float('-inf')
    
    # while stack or root:
    #     while root:
    #         stack.append(root)
    #         root = root.left
    #     root = stack.pop()
    #     # If next element in inorder traversal
    #     # is smaller than the previous one
    #     # that's not BST.
    #     if root.val <= inorder:
    #         return False
    #     inorder = root.val
    #     root = root.right

    # return True


    stack, inorder = [], float('-inf')

    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        if root.val <= inorder:
            return False
        inorder = root.val
        root = root.right
    return True