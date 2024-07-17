# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # def delNodes(
    #     self, root: Optional[TreeNode], to_delete: List[int]
    # ) -> List[TreeNode]:
    #     to_delete_set = set(to_delete)
    #     forest = []

    #     root = self._process_node(root, to_delete_set, forest)

    #     # If the root is not deleted, add it to the forest
    #     if root:
    #         forest.append(root)

    #     return forest

    # def _process_node(
    #     self, node: TreeNode, to_delete_set: Set[int], forest: List[TreeNode]
    # ) -> TreeNode:
    #     if not node:
    #         return None

    #     node.left = self._process_node(node.left, to_delete_set, forest)
    #     node.right = self._process_node(node.right, to_delete_set, forest)

    #     # Node Evaluation: Check if the current node needs to be deleted
    #     if node.val in to_delete_set:
    #         # If the node has left or right children, add them to the forest
    #         if node.left:
    #             forest.append(node.left)
    #         if node.right:
    #             forest.append(node.right)
    #         # Delete the current node by returning None to its parent
    #         return None

    #     return node

    # def delNodes(
    #     self, root: Optional[TreeNode], to_delete: List[int]
    # ) -> List[TreeNode]:
    #     if not root:
    #         return []

    #     to_delete_set = set(to_delete)
    #     forest = []

    #     nodes_queue = deque([root])

    #     while nodes_queue:
    #         current_node = nodes_queue.popleft()

    #         if current_node.left:
    #             nodes_queue.append(current_node.left)
    #             # Disconnect the left child if it needs to be deleted
    #             if current_node.left.val in to_delete_set:
    #                 current_node.left = None

    #         if current_node.right:
    #             nodes_queue.append(current_node.right)
    #             # Disconnect the right child if it needs to be deleted
    #             if current_node.right.val in to_delete_set:
    #                 current_node.right = None

    #         # If the current node needs to be deleted, add its non-null children to the forest
    #         if current_node.val in to_delete_set:
    #             if current_node.left:
    #                 forest.append(current_node.left)
    #             if current_node.right:
    #                 forest.append(current_node.right)

    #     # Ensure the root is added to the forest if it is not to be deleted
    #     if root.val not in to_delete_set:
    #         forest.append(root)

    #     return forest

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
