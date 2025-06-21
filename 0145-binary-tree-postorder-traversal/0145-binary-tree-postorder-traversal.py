# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def postorderTraversalResult(root, res):
            if not root:
                return res
            res = postorderTraversalResult(root.left, res)
            res = postorderTraversalResult(root.right, res)
            res.append(root.val)
            return res
        return postorderTraversalResult(root, [])