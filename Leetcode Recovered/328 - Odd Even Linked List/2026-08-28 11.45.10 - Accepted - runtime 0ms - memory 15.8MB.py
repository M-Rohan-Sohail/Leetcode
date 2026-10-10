# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        if head==None:
            return head
        else:
            org_head=head
            org_even=org_head.next
            odd=head
            even=head.next
            while even and even.next:
                odd.next=odd.next.next
                even.next=even.next.next
                odd=odd.next
                even=even.next
            odd.next=org_even
            return head
    
    
    