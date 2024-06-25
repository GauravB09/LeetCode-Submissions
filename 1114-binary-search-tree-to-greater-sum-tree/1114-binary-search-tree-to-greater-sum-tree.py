# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        su = 0
        def rec(curr: TreeNode):
            nonlocal su
            if curr.right:
                rec(curr.right)
            su += curr.val
            curr.val = su
            if curr.left:
                rec(curr.left)
        rec(root)
        return root