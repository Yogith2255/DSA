# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self):
        self.head=None
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp1=list1
        temp2=list2
        while(temp1!=None and temp2!=None):
            if self.head==None:
                if temp1.val>=temp2.val:
                    node=ListNode(temp2.val)
                    self.head=node
                    temp=self.head
                    temp2=temp2.next
                else:
                    node=ListNode(temp1.val)
                    self.head=node
                    temp=self.head
                    temp1=temp1.next
            else:
                    if temp1.val>=temp2.val:
                        node=ListNode(temp2.val)
                        temp=self.head
                        while temp.next!=None:
                            temp=temp.next
                        temp.next=node
                        temp2=temp2.next
                    else:
                        node=ListNode(temp1.val)
                        temp=self.head
                        while temp.next!=None:
                            temp=temp.next
                        temp.next=node
                        temp1=temp1.next
        if temp1==None:
            while temp2!=None:
                node=ListNode(temp2.val)
                temp=self.head
                if self.head is None:
                    self.head = node
                else:
                    temp = self.head
                    while temp.next is not None:
                        temp = temp.next
                    temp.next = node
                temp2=temp2.next
        else:
            while temp1!=None:
                node=ListNode(temp1.val)
                temp=self.head
                if self.head is None:
                    self.head = node
                else:
                    temp = self.head
                    while temp.next is not None:
                        temp = temp.next
                    temp.next = node
                temp1=temp1.next
        if(temp1==None and temp2==None):
            temp=self.head
            while temp!=None:
                print(temp.val,end='->')
                temp=temp.next
            print('none')
            temp=self.head
            return temp
        