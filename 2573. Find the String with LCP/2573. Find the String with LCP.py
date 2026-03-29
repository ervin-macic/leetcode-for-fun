from typing import List

class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)

        if not self._validate_basic_structure(lcp, n):
            return ""

        word = [""] * n
        next_char = ord("a")

        for i in range(n):
            if not word[i]:
                if next_char > ord("z"):
                    return ""
                word[i] = chr(next_char)
                for j in range(i + 1, n):
                    if lcp[i][j] > 0:
                        word[j] = word[i]
                next_char += 1

        if not self._verify_lcp(word, lcp, n):
            return ""

        return "".join(word)

    def _validate_basic_structure(self, lcp: List[List[int]], n: int) -> bool:
        for i in range(n):
            if lcp[i][i] != n - i:
                return False
            for j in range(n):
                if lcp[i][j] != lcp[j][i]:
                    return False
                if lcp[i][j] > min(n - i, n - j):
                    return False
        return True

    def _verify_lcp(self, word: List[str], lcp: List[List[int]], n: int) -> bool:
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if word[i] != word[j]:
                    if lcp[i][j] != 0:
                        return False
                else:
                    if i == n - 1 or j == n - 1:
                        if lcp[i][j] != 1:
                            return False
                    else:
                        if lcp[i][j] != lcp[i + 1][j + 1] + 1:
                            return False
        return True