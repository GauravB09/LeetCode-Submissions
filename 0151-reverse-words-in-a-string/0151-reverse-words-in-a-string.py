class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = 0
        word_len = 0
        word_start = 0
        s = s.strip()
        s1 = ""
        n = len(s)
        space_counted = True
        while i < n:
            if s[i] == " ":
                if not space_counted:
                    s1 += s[word_start:word_start+word_len][::-1] + " "
                    word_start = i+1
                    word_len = 0
                    space_counted = True
                else:
                    word_start = i+1
            else:
                word_len += 1
                space_counted = False
            i+=1
        return (s1 + s[word_start:word_start+word_len][::-1])[::-1]
