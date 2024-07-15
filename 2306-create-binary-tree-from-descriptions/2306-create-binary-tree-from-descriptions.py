# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def createBinaryTree(self, descriptions):
        """
        :type descriptions: List[List[int]]
        :rtype: Optional[TreeNode]
        """
        dic = {}
        child_set = set()
        n = len(descriptions)
        for i in range(n):
            parent, child, isLeft = descriptions[i]
            if parent not in dic:
                new_node = TreeNode(parent)
                dic[parent] = new_node
            if child not in dic:
                new_node = TreeNode(child)
                dic[child] = new_node
            child_set.add(child)
            if isLeft:
                dic[parent].left = dic[child]
            else:
                dic[parent].right = dic[child]
        for key in dic.keys():
            if key not in child_set:
                return dic[key]
        