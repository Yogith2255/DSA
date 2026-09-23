# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from math import gcd
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        while temp and temp.next:
            a=temp.val
            b=temp.next.val
            g = gcd(temp.val, temp.next.val)
            newNode = ListNode(g)
            nextnode = temp.next
            temp.next = newNode
            newNode.next = nextnode

            temp = nextnode
            
        return head

        