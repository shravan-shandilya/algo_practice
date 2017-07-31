class Node:
    def __init__(self,value=None,next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def add_before_head(self,node):
        node.next = self.head
        self.head = node

    def print_list(self):
        node = self.head
        while node != None:
            print node.value,
            node = node.next
        print "\n"

    def add_after_tail(self,node):
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = node
        self.tail = node

    def delete_with_key(self,key):
        node = self.head
        while node != None:
            if node.next.value == key:
                temp = node.next
                node.next = node.next.next
            node = node.next

    def reverse(self):
        node = self.head
        prev = None
        while node != None:
            curr = node
            nex = node.next
            node.next = prev
            node = nex
            prev = curr
        self.head = prev

    def is_palindrome(self):
        slow = self.head
        fast = self.head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        print slow.value,fast.value


ll = LinkedList()
ll.add_before_head(Node(1))
ll.add_before_head(Node(2))
ll.add_before_head(Node(3))
ll.add_before_head(Node(4))
ll.print_list()
ll.is_palindrome()
ll.add_before_head(Node(5))
ll.print_list()
ll.is_palindrome()
