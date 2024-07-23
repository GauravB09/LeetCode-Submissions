class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        count_dict = defaultdict(list)
        for key in freq.keys():
            count_dict[freq[key]].append(key)
        arr = []
        for key in sorted(count_dict.keys()):
            for i in sorted(count_dict[key])[::-1]:
                arr += [i] * key
        return arr
