class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        if length == 1:
            return n <= (not flowerbed[0])
        for i in range(length):
            if i == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                n -= 1
                flowerbed[i] = 1
            elif i == length - 1 and flowerbed[i] == 0 and flowerbed[i-1] == 0:
                n -= 1
                flowerbed[i] = 1
            elif flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                n -= 1
                flowerbed[i] = 1
        return n <= 0
