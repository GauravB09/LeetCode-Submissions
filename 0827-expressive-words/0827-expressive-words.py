class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        def process(st):
            if not st:
                return [], []
            chars, counts = [st[0]], [1]
            
            for i in range(1, len(st)):
                if st[i] == chars[-1]:
                    counts[-1] += 1
                else:
                    chars.append(st[i])
                    counts.append(1)
            return chars, counts
                

        ans = 0
        s_chars, s_counts = process(S)
        for word in words:
            w_chars, w_counts = process(word)
            
            if s_chars == w_chars:
                for k in range(len(w_chars)):
                    if not (w_counts[k]==s_counts[k] or (w_counts[k]<s_counts[k] and s_counts[k]>=3)):
                        break
                
                else:
                    ans+=1

        return ans