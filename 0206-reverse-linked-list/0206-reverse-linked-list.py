# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rev_node = None
        
        curr = head 
        
        while curr:
            
            newNode = ListNode(curr.val)
            
            newNode.next = rev_node
            
            rev_node = newNode
            
            curr = curr.next
            
        return rev_node
            
        