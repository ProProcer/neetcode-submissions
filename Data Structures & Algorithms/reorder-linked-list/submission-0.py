# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        root = ListNode()
        root.next = head
        slow = root
        fast = root
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        curr = slow.next
        slow.next = None
        prev = None
        while curr:
            temp = curr.next
            curr.next =prev
            prev = curr
            curr = temp
        
        left = head
        right = prev
        
        curr = root
        while left or right:
            curr.next = left
            curr = left
            left = left.next
            if right:
                curr.next = right
                curr = right
                right = right.next
        curr = root.next

        return 
