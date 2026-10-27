# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l=0
        temp=head
        while temp!=None:
            l=l+1
            temp=temp.next
        print(l)
        if l==1:
            return True
        if l%2==0:
            temp=head
            for i in range(l//2-1):
                temp=temp.next
            head1=temp.next
            temp.next=None
        else:
            temp=head
            for i in range(l//2-1):
                temp=temp.next
            head1=temp.next.next
            temp.next=None
          
        prev=None
        cn=nn=head1
        while cn!=None:
            nn=cn.next
            cn.next=prev
            prev=cn
            cn=nn
        head1=prev
        
        temp=head
        while temp!=None and head1!=None:
            if temp.val==head1.val:
                temp=temp.next
                head1=head1.next
            else:
                return False
        return True
        