# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):

        if head is None or head.next is None:
            return head

        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        sec_head = slow.next
        slow.next = None

        left = self.sortList(head)
        right = self.sortList(sec_head)

        dummy_head = ListNode(0)
        curr = dummy_head

        while left and right:
            if left.val < right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next

            curr = curr.next

        if left:
            curr.next = left

        if right:
            curr.next = right

        return dummy_head.next