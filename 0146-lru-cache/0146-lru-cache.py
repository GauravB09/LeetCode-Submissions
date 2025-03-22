from collections import deque
class LRUCache:

    def __init__(self, capacity: int):
        self.length = capacity
        self.cache = {}
        self.queue = deque()

    def get(self, key: int) -> int:
        # print("Get", self.cache)
        # print(self.queue)
        if key in self.cache:
            self.queue.remove(key)
            self.queue.append(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        # print("Put", self.cache)
        # print(self.queue)
        if key in self.cache:
            self.queue.remove(key)
        self.queue.append(key)
        if len(self.queue) == self.length + 1:
            del self.cache[self.queue.popleft()]
        self.cache[key] = value
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)