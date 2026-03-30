# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not q and not p:
            return True
        elif (q and not p) or (p and not q):
            return False
        if p.val == q.val:
            bool1 = self.isSameTree(p.left, q.left)
            bool2 = self.isSameTree(p.right, q.right)
        else:
            return False
        return bool1 and bool2