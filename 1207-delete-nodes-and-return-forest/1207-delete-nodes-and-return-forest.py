# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findParentNode(self, root: Optional[TreeNode], node_val: int) -> (Optional[TreeNode], str):
        if not root:
            return (None, "")
        if root.val == node_val:
            return (root, "S")
        if root.left and root.left.val == node_val:
            return (root, "L")
        if root.right and root.right.val == node_val:
            return (root, "R")
        left = self.findParentNode(root.left, node_val)
        if left[0]:
            return left
        return self.findParentNode(root.right, node_val)

    def getForestAfterDeletingNode(self, forest: List[TreeNode], node_val: int) -> List[TreeNode]:
        n = len(forest)
        for root_index in range(n):
            node = self.findParentNode(forest[root_index], node_val)
            if node[0]:
                if node[1] == "L":
                    if node[0].left.left:
                        forest.append(node[0].left.left)
                    if node[0].left.right:
                        forest.append(node[0].left.right)
                    node[0].left = None
                elif node[1] == "R":
                    if node[0].right.left:
                        forest.append(node[0].right.left)
                    if node[0].right.right:
                        forest.append(node[0].right.right)
                    node[0].right = None
                else:
                    if node[0].left:
                        forest.append(node[0].left)
                    if node[0].right:
                        forest.append(node[0].right)
                    forest.pop(root_index)
                return forest

    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        if not root:
            return root
        ans = [root]
        for to_del_node in to_delete:
            ans = self.getForestAfterDeletingNode(ans, to_del_node)
        return ans
