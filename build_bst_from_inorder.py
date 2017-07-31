#!/usr/bin/python
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def build_tree(inorder,start,end):
    if start >= end:
        return None

    max_index = inorder.index(max(inorder[start:end]))
    #print inorder,start,end,max_index
    root = Node(inorder[max_index])
    root.left = build_tree(inorder,start,max_index)
    root.right = build_tree(inorder,max_index+1,end)
    return root

def inorder_traversal(root):
    #print root.value,root.left,root.right
    if root.left:
        inorder_traversal(root.left)
    print root.value
    if root.right:
        inorder_traversal(root.right)

def preorder_traversal(root):
    if root:
        print root.value
        if root.left:
            preorder_traversal(root.left)
        if root.right:
            preorder_traversal(root.right)

def postorder_traversal(root):
    #print root.value,root.left,root.right
    if root:
        if root.left:
            postorder_traversal(root.left)
        if root.right:
            postorder_traversal(root.right)
        print root.value

#        40
#       /   \
#      10     30
#     /  \     \
#    5   7      28
# inoredr:  5,10,7,40,30,28
# preorder: 40,10,5,7,30,28


inorder = [5, 10, 7, 40, 30, 28]
root = build_tree(inorder,0,5)
#
print "Inoredr"
inorder_traversal(root)
print "Preoredr"
inorder_traversal(root)
print "Postoredr"
postorder_traversal(root)
