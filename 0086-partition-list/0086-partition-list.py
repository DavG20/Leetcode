# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        less = final_less = ListNode(None)
        
        greater = final_gre = ListNode(None)
        
        curr = head 
        
        while curr:
            
            if curr.val >= x:
                greater.next = ListNode(curr.val)
                greater = greater.next
            else:
                less.next = ListNode(curr.val)
                less = less.next
            curr = curr.next
        less.next = final_gre.next
        return final_less.next
        
        