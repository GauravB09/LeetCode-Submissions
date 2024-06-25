# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getSumGreaterthanRoot(self, sum_greater_than_self: int, root: TreeNode) -> int:
        # print(root, sum_greater_than_self)
        if root.left is None and root.right is None:
            sum_greater_than_self += root.val
            root.val = sum_greater_than_self
            # print("Leaf Node", root, sum_greater_than_self)
            return sum_greater_than_self
        if root.right:
            # print(self.getSumGreaterthanRoot(sum_greater_than_self, root.right))
            sum_greater_than_self = self.getSumGreaterthanRoot(sum_greater_than_self, root.right)
            # print("Right Node", root, sum_greater_than_self)
        root.val += sum_greater_than_self
        sum_greater_than_self = root.val
        curr_sum = 0
        if root.left:
            # print(self.getSumGreaterthanRoot(sum_greater_than_self, root.left))
            curr_sum = self.getSumGreaterthanRoot(sum_greater_than_self, root.left)
        #     print("Left Node", root, sum_greater_than_self, curr_sum)
        # print("Updated Node", root, sum_greater_than_self, curr_sum)
        return max(sum_greater_than_self, curr_sum)

    def bstToGst(self, root: TreeNode) -> TreeNode:
        if not root or not (root.left or root.right):
            return root
        _ = self.getSumGreaterthanRoot(0, root)
        return root
