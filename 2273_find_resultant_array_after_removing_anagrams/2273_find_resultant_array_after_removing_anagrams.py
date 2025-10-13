from typing import List
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        i = 1
        while i < len(words):
            if sorted(words[i-1]) == sorted(words[i]):
                words.remove(words[i])
            else:
                i += 1
        return words

sol = Solution()
words = ["abba","baba","bbaa","cd","cd"]
print(sol.removeAnagrams(words))