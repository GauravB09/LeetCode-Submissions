from collections import defaultdict
class Solution:
    def checkIfOneLetterDifference(self, word1: str, word2: str) -> bool:
        n = len(word1)
        count = 0
        for i in range(n):
            if word1[i] != word2[i]:
                count += 1
            if count > 1:
                return False
        return count == 1

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        n = len(wordList)
        if (endWord not in wordList):
            return 0
        queue = [beginWord]
        count = 0
        s = set()
        while queue:
            
            loop = len(queue)
            for _ in range(loop):
                start = queue[0]
                queue = queue[1:]
                if start in s:
                    continue
                s.add(start)
                for word in wordList:
                    if (self.checkIfOneLetterDifference(word, start)):
                        queue.append(word)
                if start == endWord:
                    return count + 1
            count += 1
        return 0