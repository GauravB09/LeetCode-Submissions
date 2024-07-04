# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helperFunc(self, root: Optional[TreeNode], sum: int, val: str) -> int:
        if not root:
            # print(sum)
            return sum
        val = val + str(root.val)
        if not root.left and not root.right:
            # print(val)
            return int(val)
        return self.helperFunc(root.left, sum, val) + self.helperFunc(root.right, sum, val)

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.helperFunc(root, 0, "")