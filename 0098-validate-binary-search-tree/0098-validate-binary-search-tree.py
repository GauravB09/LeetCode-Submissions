# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root, range_min, range_max):
            if not root:
                return True
            if root.val < range_min or root.val > range_max:
                return False
            l = helper(root.left, range_min, root.val-1)
            # print(l, root.left.val, range_min, root.val-1)
            r = helper(root.right, root.val+1, range_max)
            # print(r, root.right.val, root.val+1, range_max)
            return l and r
        return helper(root, -1 * ((2<<31) + 1),  ((2<<31) + 1))