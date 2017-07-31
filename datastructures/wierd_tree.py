#!/usr/bin/python
import queue
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        self.next_in_level = None
        self.inorder_next = None

class WeirdTree:
    def __init__(self):
        #         4
        #     2      6
        #   1  3   5   7
        #                10
        #               9   12
        #
        # Inorder: 1 2 3 4 5 6 7 9 10 12
        # Preorder: 4 2 1 3 6 5 7 10 9 12
        # Postorder: 1 3 2 5 9 12 10 7 6 4
        self.root = Node(4)
        self.root.left = Node(2)
        self.root.right = Node(6)
        self.root.left.left = Node(1)
        self.root.left.right = Node(3)
        self.root.right.left = Node(5)
        self.root.right.right = Node(7)
        self.root.right.right.right = Node(10)
        self.root.right.right.right.left = Node(9)
        self.root.right.right.right.right = Node(12)

    def fix_links_to_next_node_in_the_level(self):
        levels = {}
        def fix_link(root,level):
            if root == None:
                return None
            if not level in levels.keys():
                levels[level] = root
            else:
                levels[level].next_in_level = root
                levels[level] = root
            if root.left:
                fix_link(root.left,level+1)
            if root.right:
                fix_link(root.right,level+1)
        fix_link(self.root,0)

    def traverse_level_links(self,root):
        level_done = {}
        def traverse_level(root,level):
            if root == None:
                return None
            if not level in level_done.keys():
                level_done[level] = False
            else:
                level_done[level] = True
            node = root
            while node and not level_done[level]:
                print node.value,
                node = node.next_in_level
            if root.left:
                traverse_level(root.left,level+1)
            if root.right:
                traverse_level(root.right,level+1)
        traverse_level(root,1)

    def level_order(self,root):
        q = queue.Queue()
        q.push(root)
        while q.isNotEmpty():
            curr = q.pop()
            print curr.value,
            if curr.left:
                q.push(curr.left)
            if curr.right:
                q.push(curr.right)


tree = WeirdTree()
tree.fix_links_to_next_node_in_the_level()
print "\nTraverse using special pointer:\n",tree.traverse_level_links(tree.root)
print "\nLevel order traversal:\n",tree.level_order(tree.root)
