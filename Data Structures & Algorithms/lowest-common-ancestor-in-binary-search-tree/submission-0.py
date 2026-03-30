# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        res = root
        if p.val > q.val:
            p, q = q, p

        if (root.val > p.val and root.val < q.val):
            return root
        
        if root.val < p.val:
            res = self.lowestCommonAncestor(root.right, p, q)
        if root.val > q.val:
            res = self.lowestCommonAncestor(root.left, p, q)

        return res
