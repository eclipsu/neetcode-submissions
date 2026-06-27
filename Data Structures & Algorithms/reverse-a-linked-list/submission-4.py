# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        left, right = None, head

        while right:
            nxt = right.next
            right.next = left
            left = right
            right = nxt
        return left


        