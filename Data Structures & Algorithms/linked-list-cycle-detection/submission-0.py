# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        Nodes = set()

        cur = head
        while cur:
            if (cur.val, cur.next) in Nodes:
                return True
            else:
                Nodes.add((cur.val, cur.next))
            cur = cur.next
        return False