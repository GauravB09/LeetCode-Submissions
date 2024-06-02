class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        num = [0 for i in range(n)]
        dic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        ans = 0
        for i in range(n-1):
            if dic[s[i]]<dic[s[i+1]]:
                ans -= dic[s[i]]
            else:
                ans += dic[s[i]]
        return ans + dic[s[n-1]]