# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val <= list2.val:
            curr1 = list1
            curr2 = list2
        else:
            curr1 = list2
            curr2 = list1
        root = curr1
        while curr2:
            if curr1.val <= curr2.val and (curr1.next is None or curr2.val <= curr1.next.val ):
                curr1_next = curr1.next
                curr2_next = curr2.next
                curr1.next = curr2
                curr2.next = curr1_next
                curr2 = curr2_next
            curr1 = curr1.next
        return root


            