


class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
class Singly_linked_list:
    def __init__(self):
        self.head = None
    def append(self,val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node
    def traversal(self):
        if not self.head:
            print("sll is empty")
        else:
            curr = self.head
            while curr is not None:
                print(curr.val,curr.next, end = " ")
                curr = curr.next
            print()

    def insert(self, val, position):
        new_node = Node(val)

        # Insert at beginning
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return

        curr = self.head
        prev = None
        count = 0

        while curr is not None and count < position:
            prev = curr
            curr = curr.next
            count += 1

        prev.next = new_node
        new_node.next = curr
    def delete(self,val):
        temp = self.head
        if temp is None:
            print("List is empty")
            return
        if temp.val == val:
            self.head = self.head.next
            return
        else:
            found = False
            prev = None
            while temp is not None:
                if temp.val == val:
                    found = True
                    break
                prev = temp
                temp = temp.next
        if found:
            prev.next = temp.next
            return
        else:
            print("Node not found")
    def search(self,val):
        curr = self.head
        while curr is not None:
            if curr.val == val:
                return True
            curr = curr.next
        return False
    def length(self):
        curr = self.head
        count = 0
        while curr is not None:
            curr = curr.next
            count += 1
        return count
    def reverse(self):
        curr = self.head
        prev = None
        while curr is not None:
            front = curr.next
            curr.next = prev
            prev = curr
            curr = front
        return prev
def merge_two_lists(list1, list2):
    dummy = Node(0)
    tail = dummy

    while list1 and list2:

        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next

        else:
            tail.next = list2
            list2 = list2.next

        tail = tail.next

        # Attach remaining nodes
    if list1:
        tail.next = list1
    else:
        tail.next = list2

    return dummy.next


sll1 = Singly_linked_list()
sll2 = Singly_linked_list()
n1 = 5
n2 = 4
print("!!=====Start First List=====!!\n")
for i in range (n1):
    value = int(input())
    sll1.append(value)
print("!! DONE !!")
print("\n!!=====Start Second List=====!!")
for i in range (n2):
    value = int(input())
    sll2.append(value)
print("!! DONE !!")
sll1.traversal()
sll2.traversal()
merged_head = merge_two_lists(sll1.head, sll2.head)
current = merged_head
while current is not None:
    print(current.val,end = " ")
    current = current.next