# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: ListNode | None) -> ListNode | None:
        temp=head.next
        firstzero=temp
        s=0
        first=True
        while temp:
            if temp.val!=0:
                s=s+temp.val
            else:
                newnode=ListNode(s)
                if first:
                    head=newnode
                    newnode.next=temp.next
                    firstzero=newnode
                    s=0
                    first=False
                else:
                    firstzero.next = newnode
                    newnode.next = temp.next
                    firstzero = newnode
                    s = 0
            temp=temp.next
        return head

        