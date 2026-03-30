# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        somme = 0
        curr1, curr2 = l1, l2
        k = 0
        while curr1 or curr2:
            v1 = curr1.val if curr1 else 0
            v2 = curr2.val if curr2 else 0
            somme += (v1 + v2) * 10**k
            curr1 = curr1.next if curr1 else None
            curr2 = curr2.next if curr2 else None

            k += 1
        
        if somme == 0:
            return ListNode(0)
        dummy = ListNode()
        cur = dummy
        while somme != 0:
            cur.val = somme % 10
            cur.next = ListNode(somme // 10) if somme//10 != 0 else None
            somme = somme // 10
            cur = cur.next
        return dummy


        

