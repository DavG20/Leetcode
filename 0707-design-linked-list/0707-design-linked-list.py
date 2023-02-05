class Node:
    def __init__(self, val=0):
        
        self.val=val
        self.next=None
        
class MyLinkedList(object):

    def __init__(self):
        self.size=0
        self.head=None

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        temp=self.head
        if index>=0 and index<self.size:
            for i in range(index):
                temp=temp.next
            return temp.val
        else:
            return -1
            
            
        

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.addAtIndex(0,val)
        

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.addAtIndex(self.size,val)
        

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        current_node=self.head
        newNode=ListNode(val)
        if index>self.size:
            return
        if index<=0:
            newNode.next=current_node
            self.head=newNode
        else:
            for i in range(index-1):
                current_node=current_node.next
            newNode.next=current_node.next
            current_node.next=newNode
        self.size+=1
            
        

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        current_node=self.head
        
        if index>0 and index<self.size:
            for i in range(index-1):
                current_node=current_node.next
            current_node.next=current_node.next.next
        elif index==0:
            self.head=self.head.next
        else:
            return 
        self.size-=1
        