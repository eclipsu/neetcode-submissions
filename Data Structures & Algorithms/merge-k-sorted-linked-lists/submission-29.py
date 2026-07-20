# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections import deque
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
       # 1 -> 5 -> 7
       # 3 -> 4 -> 6
       # 2 -> 8

        max_heap = []

        for index, node in enumerate(lists):
            if node:
                heapq.heappush(max_heap, (node.val, index, node))

        dummy = ListNode()
        tail = dummy 

        while max_heap:
            value, index, node = heapq.heappop(max_heap)

            tail.next = node 

            if node.next:
                heapq.heappush(max_heap, (node.next.val, index, node.next))

            tail = tail.next
        return dummy.next