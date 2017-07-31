#!/usr/bin/python
import queue
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self,complex=False):
        if not complex:
            #        4
            #     2      6
            #   1  3   5   7
            #                15
            #               10  20
            self.root = Node(4)
            self.root.left = Node(2)
            self.root.right = Node(6)
            self.root.left.left = Node(1)
            self.root.left.right = Node(3)
            self.root.right.left = Node(5)
            self.root.right.right = Node(7)
            self.root.right.right.right = Node(15)
            self.root.right.right.right.left = Node(10)
            self.root.right.right.right.right = Node(20)
        else:
            #                   10
            #                  5    12
            #               3   8   11  13
            #             1 4  6 9        16
            #                           14   20
            self.root = Node(10)
            self.root.left = Node(5)
            self.root.right = Node(12)
            self.root.left.left = Node(3)
            self.root.left.right = Node(8)
            self.root.left.left.left = Node(1)
            self.root.left.left.right = Node(4)
            self.root.left.right.left = Node(6)
            self.root.left.right.right = Node(9)
            self.root.right.left = Node(11)
            self.root.right.right = Node(13)
            self.root.right.right.right = Node(16)
            self.root.right.right.right.left = Node(14)
            self.root.right.right.right.right = Node(20)

    def inorder(self,root):
        if root.left:
            self.inorder(root.left)
        if root:
            print root.value,
        if root.right:
            self.inorder(root.right)

    def preorder(self,root):
        if root:
            print root.value,
            if root.left:
                self.preorder(root.left)
            if root.right:
                self.preorder(root.right)

    def find(self,root,data):
        if root.value == data:
            return root
        if data < root.value:
            return self.find(root.left,data)
        else:
            return self.find(root.right,data)

    def inorder_successor(self,root,relative_to):
        if root == None:
            return None
        node = self.find(root,relative_to)
        if node == None:
            return
        #case 1: right subtree is found
        #return leftmost node of right subtree
        if node.right:
            curr = node.right
            while curr.left != None:
                curr = curr.left
            return curr
        #case 2: right subree not found
        #return a parent for which this node is in the left subtree.
        else:
            ancestor = None
            curr = root
            while True:
                if (relative_to < curr.value) and (curr.left != None) and (curr.right != None):
                    ancestor = curr
                    curr = curr.left
                elif relative_to > curr.value:
                    curr = curr.right
                if curr.value == relative_to:
                    break
            return ancestor

    def inorder_predecessor(self,root,relative):
        if root == None:
            return None
        node  = self.find(root,relative)
        if node == None:
            return  None

        #case 1: Node has the left subtree. then the predecessor is the right most node of the lfet subtree.
        if node.left:
            curr = node.left
            while curr.right != None:
                curr = curr.right
            return curr
        #case 2: Node doesnot have left subtree., then the predecessor is the ancestor to which this node is on the right subtree.
        else:
            ancestor = None
            curr = root
            while True:
                if (relative < curr.value) and (curr.left != None):
                    curr = curr.left
                elif (relative > curr.value) and (curr.right != None):
                    ancestor = curr
                    curr = curr.right
                if relative == curr.value:
                    break
            return ancestor

    def preorder_predecessor(self,root,relative):
        if root == None:
            return None

        curr_parent = None
        curr = root
        side = None
        while True:
            if (curr.value > relative):
                curr_parent = curr
                curr = curr.left
                side = True
            elif (curr.value < relative):
                curr_parent = curr
                curr = curr.right
                side = False
            if relative == curr.value:
                break
        if side:
            return curr_parent
        else:
            return curr_parent.left

    def preorder_successor(self,root,relative):
        if root == None:
            return None
        ancestor_with_right = None
        curr = root
        while True:
            if (curr.right) and (curr.right.value != relative):
                ancestor_with_right = curr
            if relative < curr.value:
                curr = curr.left
            elif relative > curr.value:
                curr = curr.right
            if curr.value == relative:
                break

        if curr.left:
            return curr.left
        elif curr.right:
            return curr.right
        elif (curr.left == None) and (curr.right == None):
            return ancestor_with_right.right


t = Tree(complex=True)
print "\nInorder(before):"
t.inorder(t.root)
print "\nInorder successor for 1:",t.inorder_successor(t.root,1).value
print "\nInorder successor for 3:",t.inorder_successor(t.root,3).value
print "\nInorder successor for 5:",t.inorder_successor(t.root,5).value
#print "\n Inorder successor for 8:",t.inorder_successor(t.root,8).value


#print "\n Inorder Predecessor for 1:",t.inorder_predecessor(t.root,1).value
print "\nInorder Predecessor for 3:",t.inorder_predecessor(t.root,3).value
print "\nInorder Predecessor for 5:",t.inorder_predecessor(t.root,5).value
print "\nInorder Predecessor for 8:",t.inorder_predecessor(t.root,8).value

print "\nPreorder:"
t.preorder(t.root)
print "\nPreorder Predecessor for 1:",t.preorder_predecessor(t.root,1).value
print "\nPreorder Predecessor for 3:",t.preorder_predecessor(t.root,3).value
print "\nPreorder Predecessor for 5:",t.preorder_predecessor(t.root,5).value
print "\nPreorder Predecessor for 8:",t.preorder_predecessor(t.root,8).value
#print "\nPreorder Predecessor for 10:",t.preorder_predecessor(t.root,10).value


print "\nPreorder successor for 1:",t.preorder_successor(t.root,1).value
print "\nPreorder successor for 3:",t.preorder_successor(t.root,3).value
print "\nPreorder successor for 5:",t.preorder_successor(t.root,5).value
print "\nPreorder successor for 8:",t.preorder_successor(t.root,8).value
print "\nPreorder successor for 10:",t.preorder_successor(t.root,10).value
print "\nPreorder successor for 13:",t.preorder_successor(t.root,13).value
print "\nPreorder successor for 16:",t.preorder_successor(t.root,16).value
print "\nPreorder successor for 14:",t.preorder_successor(t.root,14).value
print "\nPreorder successor for 12:",t.preorder_successor(t.root,12).value
print "\nPreorder successor for 11:",t.preorder_successor(t.root,11).value
