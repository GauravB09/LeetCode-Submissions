# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def findAndStoreRouteToLeafs(self, root):
    #     if not root:
    #         return
    #     if not root.left and not root.right:
    #         self.routeList.append("".join(self.route))
    #     if root.left:
    #         self.route.append("L")
    #         self.findAndStoreRouteToLeafs(root.left)
    #         self.route.pop()
    #     if root.right:
    #         self.route.append("R")
    #         self.findAndStoreRouteToLeafs(root.right)
    #         self.route.pop()

    # def countPairs(self, root: TreeNode, distance: int) -> int:
    #     self.routeList = []
    #     self.route = []
    #     self.findAndStoreRouteToLeafs(root)
    #     n = len(self.routeList)
    #     ans = 0
    #     for i in range(n-1):
    #         for j in range(i+1, n):
    #             k = 0
    #             str1 = self.routeList[i]
    #             len_str1 = len(str1)
    #             str2 = self.routeList[j]
    #             len_str2 = len(str2)
    #             while k < len_str1 and k < len_str2 and str1[k] == str2[k]:
    #                 k += 1
    #             if len_str1 - k + len_str2 - k <= distance:
    #                 ans += 1
    #     return ans

    # def _post_order(self, currentNode, distance):
    #     if currentNode is None:
    #         return [0] * 12
    #     elif currentNode.left is None and currentNode.right is None:
    #         current = [0] * 12
    #         # Leaf node's distance from itself is 0
    #         current[0] = 1
    #         return current

    #     # Leaf node count for a given distance i
    #     left = self._post_order(currentNode.left, distance)
    #     right = self._post_order(currentNode.right, distance)

    #     current = [0] * 12

    #     # Combine the counts from the left and right subtree and shift by
    #     # +1 distance
    #     for i in range(10):
    #         current[i + 1] += left[i] + right[i]

    #     # Initialize to total number of good leaf nodes pairs from left and right subtrees.
    #     current[11] = left[11] + right[11]

    #     # Iterate through possible leaf node distance pairs
    #     for d1 in range(distance + 1):
    #         for d2 in range(distance + 1):
    #             if 2 + d1 + d2 <= distance:
    #                 # If the total path distance is less than the given distance limit,
    #                 # then add to he total number of good pairs
    #                 current[11] += left[d1] * right[d2]

    #     return current

    # def countPairs(self, root: TreeNode, distance: int) -> int:
    #     return self._post_order(root, distance)[11]

    def _traverse_tree(self, curr_node, prev_node, graph, leaf_nodes):
        if curr_node is None:
            return
        if curr_node.left is None and curr_node.right is None:
            leaf_nodes.add(curr_node)
        if prev_node is not None:
            if prev_node not in graph:
                graph[prev_node] = []
            graph[prev_node].append(curr_node)

            if curr_node not in graph:
                graph[curr_node] = []
            graph[curr_node].append(prev_node)

        self._traverse_tree(curr_node.left, curr_node, graph, leaf_nodes)
        self._traverse_tree(curr_node.right, curr_node, graph, leaf_nodes)

    def countPairs(self, root, distance):
        graph = {}
        leaf_nodes = set()

        self._traverse_tree(root, None, graph, leaf_nodes)

        ans = 0

        for leaf in leaf_nodes:
            bfs_queue = []
            seen = set()
            bfs_queue.append(leaf)
            seen.add(leaf)
            for i in range(distance + 1):
                # Clear all nodes in the queue (distance i away from leaf node)
                # Add the nodes' neighbors (distance i+1 away from leaf node)
                size = len(bfs_queue)
                for j in range(size):
                    curr_node = bfs_queue.pop(0)
                    if curr_node in leaf_nodes and curr_node != leaf:
                        ans += 1
                    if curr_node in graph:
                        for neighbor in graph.get(curr_node):
                            if neighbor not in seen:
                                bfs_queue.append(neighbor)
                                seen.add(neighbor)
        return ans // 2