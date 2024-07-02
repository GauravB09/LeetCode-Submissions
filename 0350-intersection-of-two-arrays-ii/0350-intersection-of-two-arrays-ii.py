class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count_1 = Counter(nums1)
        arr = []
        for i in nums2:
            if i in count_1:
                arr.append(i)
                count_1[i] -= 1
                if count_1[i] == 0:
                    count_1.pop(i)
        return arr