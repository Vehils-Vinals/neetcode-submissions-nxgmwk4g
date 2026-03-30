# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1, cur2 = l1, l2

        Somme = 0
        compt = 0
        while cur1 or cur2:
            if cur1 and cur2:
                Somme += cur1.val * 10**compt + cur2.val * 10**compt
            elif cur1:
                Somme += cur1.val * 10**compt
            else: 
                Somme += cur2.val * 10**compt
            compt += 1
            if cur1:
                cur1 = cur1.next
            if cur2:
                cur2 = cur2.next

        if Somme != 0:
            l = math.floor(math.log10(Somme))
        else: 
            return ListNode()

        ans = ListNode()
        head = ans
        for i in range(l+1):
            ans.val = Somme % 10
            Somme = Somme // 10
            if Somme != 0:
                ans.next = ListNode()
                ans = ans.next
        
        return head


