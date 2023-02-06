class Solution(object):
    def reverseKGroup(self,head,k):
        count_node=current_node=head 
        size=0
        newNode=newhead=ListNode(-1)
        if head is None:
            return head 
        while count_node:
            size+=1
            count_node=count_node.next 
        ranges=int(size//k)
        for i in range(ranges):
            prev_node=None
            j=0
            while j<k:
                next_node=current_node.next 
                current_node.next=prev_node
                prev_node=current_node
                current_node=next_node
                j+=1
            newhead.next=prev_node
            for i in range(k):
                newhead=newhead.next 
        newhead.next=current_node
        return newNode.next