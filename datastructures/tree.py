#!/usr/bin/python
import queue
import stack

class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
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

    def preorder_iterative(self,root):
        if root == None:
            return None
        s = stack.Stack()
        s.push(root)
        while not s.empty():
            temp = s.pop()
            print temp.value,
            if temp.right:
                s.push(temp.right)
            if temp.left:
                s.push(temp.left)

    def postorder(self,root):
        if root.left:
            self.postorder(root.left)
        if root.right:
            self.postorder(root.right)
        if root:
            print root.value,

    def postorder_iterative(self,root):
        if root == None:
            return None
        s = stack.Stack()
        while True:
            while root:
                if root.right:
                    s.push(root.right)
                s.push(root)
                root = root.left
            root = s.pop()
            if root.right and (s.top() == root.right):
                s.pop()
                s.push(root)
                root = root.right
            else:
                print root.value,
                root = None
            if s.empty():
                break


    def levelorder(self,root):
        q = queue.Queue()
        q.push(root)
        while q.isNotEmpty():
            curr = q.pop()
            print curr.value,
            if curr.left:
                q.push(curr.left)
            if curr.right:
                q.push(curr.right)

    def spiral(self,root):
        q = queue.Queue()
        q.push(root)
        ltr = True
        while q.isNotEmpty():
            curr = q.pop()
            print curr.value
            if ltr:
                if curr.left:
                    q.push(curr.left)
                if curr.right:
                    q.push(curr.right)
            else:
                if curr.right:
                    q.push(curr.right)
                if curr.left:
                    q.push(curr.left)
            ltr = not ltr

    def print_left_view(self):
        self.left_view_dict = {}
        self.left_view(self.root,1)
        self.left_view_dict = {}

    def left_view(self,root,level):
        if not level in self.left_view_dict.keys():
            self.left_view_dict[level] = root.value
            print "Level #",level,":",root.value
        if root.left:
            self.left_view(root.left,level+1)
        if root.right:
            self.left_view(root.right,level+1)

    def mirror(self,root):
        if root.right:
            self.mirror(root.right)
        if root.left:
            self.mirror(root.left)
        root.left,root.right = root.right,root.left

    def depth(self,root):
        if root.left:
            left_depth = self.depth(root.left)
        else:
            left_depth = 0
        if root.right:
            right_depth = self.depth(root.right)
        else:
            right_depth = 0
        return max(left_depth,right_depth) + 1

    def count_leaves(self,root):
        if root == None:
            return 0
        if (root.left == None) and (root.right == None):
            return 1
        return self.count_leaves(root.left)+self.count_leaves(root.right)

    def width(self,root):
        if root == None:
            return 0
        #One obvious choice for max width will be sum of heights of left and right subtrees and the root
        lwidth = 0
        rwidth = 0
        obvious_choice = 0
        if root.left:
            obvious_choice += self.depth(root.left)
            lwidth = self.width(root.left)
        if root.right:
            obvious_choice += self.depth(root.right)
            rwdith = self.width(root.right)
        obvious_choice+=1
        return max(obvious_choice,max(lwidth,rwidth))

    def width_bounds(self,root,minimum,maximum,relative_index):
        if root == None:
            return None
        if relative_index < minimum:
            minimum = relative_index
        if relative_index > maximum:
            maximum = relative_index
        if root.left:
            minimum,maximum = self.width_bounds(root.left,minimum,maximum,relative_index-1)
        if root.right:
            minimum,maximum = self.width_bounds(root.right,minimum,maximum,relative_index+1)
        return [minimum,maximum]

    def vertical(self,root,curr_index,relative_index):
        if root == None:
            return None

        if curr_index == relative_index:
            print root.value,

        if root.left:
            self.vertical(root.left,curr_index-1,relative_index)
        if root.right:
            self.vertical(root.right,curr_index+1,relative_index)

    def vertical_order(self,root):
        min_index,max_index = self.width_bounds(root,0,0,0)
        for i in range(min_index,max_index+1):
            print "\nRelative Index:",i
            self.vertical(root,0,i)

    def toppest(self,root,curr_index,relative_index,topview):
        if root == None:
            return None
        if (curr_index == relative_index) and not(curr_index in topview.keys()):
            print root.value
            topview[curr_index] = root.value
        self.toppest(root.left,curr_index-1,relative_index,topview)
        self.toppest(root.right,curr_index+1,relative_index,topview)

    def top_view(self,root):
        topview = {}
        min_index,max_index = self.width_bounds(root,0,0,0)
        for i in range(min_index,max_index+1):
            self.toppest(root,0,i,topview)

    def left_and_right_view(self,root):
        left = {}
        right = {}
        def level_view(root,level):
            if root == None:
                return None
            if not level in left.keys():
                left[level] = root.value
            right[level] = root.value
            if root.left:
                level_view(root.left,level+1)
            if root.right:
                level_view(root.right,level+1)
        level_view(root,0)
        for i in range(0,len(left.keys())):
            print "Left:", left[i],"  Right:",right[i]

    def has_sum_path(self,root,summ,path):
        if root == None:
            return None
        summ -= root.value
        path.append(root.value)
        if (summ == 0) and (root.left == None) and (root.right == None):
            print path
            return True
        left = right = False
        if root.left:
                left = self.has_sum_path(root.left,summ,path)
                path.pop()
        if root.right:
                right = self.has_sum_path(root.right,summ,path)
                path.pop()
        return left or right

    def all_root_to_leaf(self,root,path):
        if root  == None:
            return None
        path.append(root.value)
        if root.left == None and root.right == None:
            print path
            return
        if root.left:
            self.all_root_to_leaf(root.left,path)
            path.pop()
        if root.right:
            self.all_root_to_leaf(root.right,path)
            path.pop()

    def double_tree(self,root):
        if root == None:
            return None
        temp = root.left
        root.left = Node(root.value)
        root.left.left = self.double_tree(temp)
        root.right = self.double_tree(root.right)
        return root

    def levelwise_width(self,root):
        levels = {}
        def level_width(root,level):
            if root == None:
                return None
            if not level in levels.keys():
                levels[level] = 1
            else:
                levels[level] += 1
            #print "Current Level:",level,"Level value:",root.value, "Dict: ",levels
            if root.left:
                level_width(root.left,level+1)
            if root.right:
                level_width(root.right,level+1)
        level_width(root,1)
        print levels

    def radial_print(self,root,distance):
        if root == None:
            return None
        if distance == 0:
            print root.value,
        else:
            if root.left:
                self.radial_print(root.left,distance-1)
            if root.right:
                self.radial_print(root.right,distance-1)

    def print_path_to_key(self,root,key,path=[]):
        if root == None:
            return None
        if root.value == key:
            print path
            return
        else:
            path.append(root.value)
        if root.left:
            self.print_path_to_key(root.left,key,path)
            path.pop()
        if root.right:
            self.print_path_to_key(root.right,key,path)
            path.pop()

    def is_sum_tree(self,root):
        if root == None:
            return
        left_sum = self.is_sum_tree(root.left)
        right_sum = self.is_sum_tree(root.right)
        if left_sum and right_sum:
            if left_sum+right_sum == root.value:
                return left_sum+right_sum+root.value
            else:
                return -1

    def vertical_sum(self,root):
        sums = {}
        def compute_vertical_sum(root,relative_index):
            #print root.value,relative_index
            if root == None:
                return None
            if not relative_index in sums.keys():
                sums[relative_index] = root.value
            else:
                sums[relative_index] += root.value
            if root.left:
                compute_vertical_sum(root.left,relative_index-1)
            if root.right:
                compute_vertical_sum(root.right,relative_index+1)
        compute_vertical_sum(root,0)
        print sums

    def max_sum_root_to_leaf(self,root):
        global maximum
        maximum = 0
        def root_to_leaf_sum(root,path):
            if root == None:
                return 0
            if (root.left == None) and (root.right == None):
                global maximum
                if sum(path)+root.value > maximum:
                    maximum = sum(path)+root.value
            path.append(root.value)
            if root.left:
                root_to_leaf_sum(root.left,path)
                path.pop()
            if root.right:
                root_to_leaf_sum(root.right,path)
                path.pop()
        root_to_leaf_sum(root,[])
        return maximum

    def print_left_boundary(self,root,direction=True):
        if root == None:
            return None
        if root.left:
            if direction:
                print root.value
            self.print_left_boundary(root.left,direction)
            if not direction:
                print root.value
        elif root.right:
            if direction:
                print root.value
            self.print_left_boundary(root.right,direction)
            if not direction:
                print root.value

    def print_right_boundary(self,root,direction):
        if root == None:
            return None
        if root.right:
            if direction:
                print root.value
            self.print_right_boundary(root.right,direction)
            if not direction:
                print root.value
        elif root.left:
            if direction:
                print root.value
            self.print_right_boundary(root.left,direction)
            if not direction:
                print root.value

    def print_leaves(self,root,direction):
        if root == None:
            return None

        if (root.left == None) and (root.right == None):
            print root.value
            return

        if direction:
            if root.left:
                self.print_leaves(root.left,direction)
            if root.right:
                self.print_leaves(root.right,direction)
        else:
            if root.right:
                self.print_leaves(root.right,direction)
            if root.left:
                self.print_leaves(root.left,direction)

    def lca(self,root,node1,node2):
        if root == None:
            return None
        if root.value == node1 or root.value == node2:
            return root
        left = self.lca(root.left,node1,node2)
        right = self.lca(root.right,node1,node2)

        if left and right:
            return root

        if left:
            return left
        else:
            return right
    def find_lca(self,root,node1,node2):
        if root == None:
            return None
        if (node1 < root.value) and  (node2 < root.value):
            return self.find_lca(root.left,node1,node2)
        elif (node1 > root.value) and  (node2 > root.value):
            return self.find_lca(root.right,node1,node2)
        elif ((node1 < root.value) and (node2 > root.value)) or ((node1 > root.value) and (node2 < root.value)):
            return root.value

tree = BinaryTree()
print "\nInorder"
tree.inorder(tree.root)
print "\nPreorder"
tree.preorder(tree.root)
print "\nPostorder"
tree.postorder(tree.root)
print "\nLevelorder"
tree.levelorder(tree.root)
print "\nLeft View"
tree.print_left_view()
print "\nMirror'ing"
print "\nInorder before mirroring"
tree.inorder(tree.root)
tree.mirror(tree.root)
print "\nInorder after mirroring"
tree.inorder(tree.root)
print "\nLeftview after mirroring"
tree.print_left_view()
print "mirroring again"
tree.mirror(tree.root)
print "Depth:",tree.depth(tree.root)
print "Width:",tree.width(tree.root)
print "Leaves count:",tree.count_leaves(tree.root)
print "\nSpiral:"
tree.spiral(tree.root)
print "\nWidth bounds relative to root:",tree.width_bounds(tree.root,0,0,0)

print "\nVertical Order:",tree.vertical_order(tree.root)
print "\nTop View:",tree.top_view(tree.root)

#print "\nChildren sum property:",tree.check_children_sum_property(tree.root)
print "\nLeft and right view:",tree.left_and_right_view(tree.root)
print "\nSumPath of 39:\n",tree.has_sum_path(tree.root,39,[])
print "\nSumPath of 15:\n",tree.has_sum_path(tree.root,15,[])
print "\nSumPath of 12:\n",tree.has_sum_path(tree.root,12,[])
print "\nAll root to leafs\n",tree.all_root_to_leaf(tree.root,[])
#print "\n double tree:"
#tree.double_tree(tree.root)
#print "\n Inorder after doubling:\n",tree.inorder(tree.root)
print "\nLevelwise width:",tree.levelwise_width(tree.root)
print "\nPrint nodes at distance 4 from root\n",tree.radial_print(tree.root,4)

print "\nPrint path to key 12\n",tree.print_path_to_key(tree.root,12)
print "\nis sum tree\n",tree.is_sum_tree(tree.root)

print "\nVertical sum\n"
tree.vertical_sum(tree.root)
print "\nmax. sum path"
print tree.max_sum_root_to_leaf(tree.root)

print "\nPrint left boundary:"
tree.print_left_boundary(tree.root,False)

print "\Print right boundary:"
tree.print_right_boundary(tree.root,False)

print "\nPrint leaves"
tree.print_leaves(tree.root,False)

print "\n LCA of 9 and 12 is",tree.lca(tree.root,9,12).value
print "\n LCA of 5 and 12 is",tree.lca(tree.root,5,12).value
print "\n LCA of 3 and 12 is",tree.lca(tree.root,3,12).value

print "\n LCA of 9 and 12 is",tree.find_lca(tree.root,9,12)
print "\n LCA of 5 and 12 is",tree.find_lca(tree.root,5,12)
print "\n LCA of 3 and 12 is",tree.find_lca(tree.root,3,12)

print "\n Preorder Iterative",
tree.preorder_iterative(tree.root)
print "\n Preorder Recursive",
tree.preorder(tree.root)

print "\n Postorder Iterative",
tree.postorder_iterative(tree.root)
print "\n Postorder Recursive",
tree.postorder(tree.root)
