# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        curr = head
        while curr:
            curr = curr.next
            l += 1
        
        stop = l - n
        if stop == 0:
            return head.next
        count = 0
        prev, curr = head, head
        while curr:
            if count == stop:
                tmp = curr.next
                curr = prev
                curr.next = tmp
                return head
            prev = curr
            curr = curr.next
            count += 1
