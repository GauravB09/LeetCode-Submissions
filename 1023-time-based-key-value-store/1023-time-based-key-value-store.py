from collections import defaultdict
class TimeMap:
    def binarySearch(self, arr, target):
        # print("Bin", arr, target)
        low = 0
        high = len(arr) - 1
        ans = 0
        while low <= high:
            mid = (low + high)//2
            # print("Bin1", low, high, mid, arr[mid])
            # if arr[mid][0] == target:
            #     return mid
            if arr[mid][0] <= target:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans

    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_map:
            self.time_map[key] = [[0, ""]]
        self.time_map[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""
        curr_key_list = self.time_map[key]
        correct_index = self.binarySearch(curr_key_list, timestamp)
        # print(timestamp, curr_key_list, correct_index)
        return curr_key_list[correct_index][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)