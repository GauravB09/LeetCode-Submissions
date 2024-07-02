class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count_1 = Counter(nums1)
        count_2 = Counter(nums2)
        arr = []
        for i in count_1:
            if i in count_2:
                arr += [i] * min(count_1[i], count_2[i])
        return arr