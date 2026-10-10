# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        count_fast=0
        slow=head
        fast=head
        while count_fast<n:
            fast=fast.next
            count_fast+=1
        if fast==None:
            return head.next
        while fast and fast.next:
                slow=slow.next
                fast=fast.next
        temp=slow.next
        slow.next=slow.next.next
        temp.next=None
        return head
