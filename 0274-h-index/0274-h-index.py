class Solution:
    def hIndex(self, citations: List[int]) -> int:
        max_elem = -1
        n = len(citations)
        for i in range(n):
            if max_elem<citations[i]:
                max_elem = citations[i]
        cnt = [0 for i in range(max_elem + 2)]
        for i in range(n):
            cnt[citations[i]] += 1
        for i in range(max_elem, -1 , -1):
            cnt[i] += cnt[i+1]
            if cnt[i] >= i:
                return i