def preorder(node):
    if node == None:
        return
    print(node.val)
    preorder(node.left)
    preorder(node.right)