class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        return list(set(edges[0]).intersection(set(edges[1])))[0]