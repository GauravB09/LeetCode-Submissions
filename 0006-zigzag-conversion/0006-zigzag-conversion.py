class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        n = len(s)
        if n <= numRows or numRows == 1 :
            return s
        else:
            s1 = ""
            j = 0
            while j<numRows:
                i = j
                k = 0
                while i<n:
                    if j == 0 or j == numRows-1:
                        s1 += s[i]
                        i+=2*(numRows-2) + 2
                    else:
                        arr = [2*(numRows-j-2) + 2, 2*(j-1) + 2]
                        s1 += s[i]
                        i += arr[k%2]
                        k+=1
                j+=1
            return s1