# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        root = ListNode()
        heap = [(n.val, i) for i, n in enumerate(lists) if n]
        if not heap:
            return 
        heapq.heapify(heap)
        
        curr = root
        while len(heap) > 1:
            _, idx = heapq.heappop(heap)
            min_node = lists[idx]
            curr.next = min_node
            curr = curr.next
            lists[idx] = min_node.next
            if lists[idx]:
                heapq.heappush(heap, (lists[idx].val, idx))
        curr.next = lists[heap[0][1]]
        return root.next


            
                
                    