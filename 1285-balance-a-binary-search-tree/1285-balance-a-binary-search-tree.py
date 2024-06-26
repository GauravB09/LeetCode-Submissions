# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def lengthOfTree(self, root: TreeNode) -> Int:
    #     if not root:
    #         return -1
    #     if not (root.left or root.right):
    #         return 0
    #     return max(self.lengthOfTree(root.left), self.lengthOfTree(root.right)) + 1

    # def shiftLeft(self, root: TreeNode) -> TreeNode:
    #     if not root or not (root.left or root.right):
    #         return root
    #     right_subtree = root.right
    #     right_subtree.left = root
    #     right_subtree.left.right = None
    #     return right_subtree
    
    # def shiftRight(self, root: TreeNode) -> TreeNode:
    #     if not root or not (root.left or root.right):
    #         return root
    #     left_subtree = root.left
    #     left_subtree.right = root
    #     left_subtree.right.left = None
    #     return left_subtree
    def preorderTraversal(self, root: TreeNode, arr: [int]) -> [int]:
        if not root:
            return arr
        if not(root.left or root.right):
            arr.append(root.val)
            return arr
        if root.left:
            arr = self.preorderTraversal(root.left, arr)
        arr.append(root.val)
        if root.right:
            arr = self.preorderTraversal(root.right, arr)
        return arr

    def buildBalanceTree(self, arr: [int], left: int, right: int) -> TreeNode:
        node = None 
        if left <= right:
            mid = left + ((right - left) // 2)
            # print(left, right, mid, arr[mid], arr)
            node = TreeNode(arr[mid])
            node.left = self.buildBalanceTree(arr, left, mid-1)
            node.right = self.buildBalanceTree(arr, mid+1, right)
        return node


    def balanceBST(self, root: TreeNode) -> TreeNode:
        arr = self.preorderTraversal(root, [])
        n = len(arr)
        return self.buildBalanceTree(arr,0, n-1)