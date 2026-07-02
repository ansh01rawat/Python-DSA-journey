# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        while fast and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        if fast:
            slow = slow.next
        temp = slow
        prev = None
        while temp is not None:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        new_node = head
        while new_node and prev is not None:
            if new_node.val == prev.val:
                new_node = new_node.next
                prev = prev.next
            else:
                return False
        return True

