# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        while temp and temp.next:
            a=temp.val
            b=temp.next.val
            for i in range(min(a,b),0,-1):
                if a%i==0 and b%i==0:
                    newNode=ListNode(i)
                    nextnode=temp.next
                    temp.next=newNode
                    newNode.next=nextnode
                    break
            temp=newNode.next
        return head

        