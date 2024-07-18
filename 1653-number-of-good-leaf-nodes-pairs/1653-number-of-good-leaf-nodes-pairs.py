# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findAndStoreRouteToLeafs(self, root):
        if not root:
            return
        if not root.left and not root.right:
            self.routeList.append("".join(self.route))
        if root.left:
            self.route.append("L")
            self.findAndStoreRouteToLeafs(root.left)
            self.route.pop()
        if root.right:
            self.route.append("R")
            self.findAndStoreRouteToLeafs(root.right)
            self.route.pop()


    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.routeList = []
        self.route = []
        self.findAndStoreRouteToLeafs(root)
        n = len(self.routeList)
        ans = 0
        for i in range(n-1):
            for j in range(i+1, n):
                k = 0
                str1 = self.routeList[i]
                len_str1 = len(str1)
                str2 = self.routeList[j]
                len_str2 = len(str2)
                while k < len_str1 and k < len_str2 and str1[k] == str2[k]:
                    k += 1
                if len_str1 - k + len_str2 - k <= distance:
                    ans += 1
        return ans