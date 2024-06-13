# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def getMirrorImage(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    #     if not root:
    #         return
    #     new_root = TreeNode()
    #     new_root.val = root.val
    #     new_root.left = self.getMirrorImage(root.right)
    #     new_root.right = self.getMirrorImage(root.left)
    #     return new_root

    # def checkIfSameTree(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    #     if not root1 and not root2:
    #         return True
    #     elif root1 and root2:
    #         return root1.val == root2.val and self.checkIfSameTree(root1.left, root2.left) and self.checkIfSameTree(root1.right, root2.right)
    #     else:
    #         return False

    def isSameVal(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return (not root1 and not root2) or (root1 and root2 and root1.val == root2.val and self.isSameVal(root1.left, root2.right) and self.isSameVal(root1.right, root2.left))

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # new_tree = self.getMirrorImage(root)
        # return self.checkIfSameTree(root, new_tree)
        return not root or self.isSameVal(root.left, root.right)