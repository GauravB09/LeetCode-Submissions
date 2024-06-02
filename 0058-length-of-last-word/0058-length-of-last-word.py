class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        ans = 0
        boolean = False
        for i in range(n-1, -1 ,-1):
            if s[i]==" ":
                if boolean:
                    return ans
                else:
                    continue
            else:
                boolean = True
                ans += 1
        return ans
