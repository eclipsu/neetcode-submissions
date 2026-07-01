# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next or not head.next.next: return

        # Find the mid of the LL 
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # First half and Second half is now split, 
        second = slow.next
        prev = slow.next = None

        # Reverse the 2nd half
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # Merge them
        first = head
        second = prev
                
        while second:
            temp_first = first.next
            temp_second = second.next

            first.next = second
            second.next = temp_first

            first = temp_first
            second = temp_second
        

            

