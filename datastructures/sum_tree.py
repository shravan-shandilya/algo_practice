#!/usr/bin/python
import queue
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        #         10
        #     -2      6
        #   8  -4   7   5
        #
        # Inorder: 1 2 3 4 5 6 7 9 10 12
        # Preorder: 4 2 1 3 6 5 7 10 9 12
        # Postorder: 1 3 2 5 9 12 10 7 6 4
        self.root = Node(10)
        self.root.left = Node(-2)
        self.root.right = Node(6)
        self.root.left.left = Node(8)
        self.root.left.right = Node(-4)
        self.root.right.left = Node(7)
        self.root.right.right = Node(5)

    def inorder(self,root):
        if root.left:
            self.inorder(root.left)
        if root:
            print root.value,
        if root.right:
            self.inorder(root.right)

    def convert_to_sum_tree(self,root):
        def convert(root):
            #print root.value
            if root == None:
                return 0
            if (root.left == None) and (root.right == None):
                temp = root.value
                root.value = 0
                return temp
            root.value = 0
            if root.left:
                root.value += convert(root.left)
            if root.right:
                root.value += convert(root.right)
            return root.value
        convert(root)

    def iterative_height(self,root):
        if root == None:
            return None

        q = queue.Queue()
        q.push(root)
        height = 0
        while True:
            nodes_in_level = q.length()
            if nodes_in_level == 0:
                return height
            height += 1
            while nodes_in_level > 0:
                node = q.pop()
                if node.left:
                    q.push(node.left)
                if node.right:
                    q.push(node.right)
                nodes_in_level -= 1
t = Tree()
print "\n Inorder(before):"
t.inorder(t.root)
print "\n Converting to sum tree:"
t.convert_to_sum_tree(t.root)
print "\n Inorder(after):"
t.inorder(t.root)
print "\n Height iterative:",t.iterative_height(t.root)
