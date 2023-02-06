# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res=[]
        for i in range(len(lists)):
            curr=lists[i]
            while curr:
                res.append(curr.val)
                curr=curr.next
        res.sort()
        newNode=sorted_List=ListNode(-10001)
        for num in res:
            sorted_List.next=ListNode(num)
            sorted_List=sorted_List.next
        return newNode.next
            