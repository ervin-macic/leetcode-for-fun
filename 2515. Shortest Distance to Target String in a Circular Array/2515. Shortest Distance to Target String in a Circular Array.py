from typing import List
class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if words[startIndex] == target:
            return 0
        n = len(words)
        # go left 
        i = (startIndex - 1) % n
        left_steps = 1
        while i != startIndex and words[i] != target:
            i -= 1
            i %= n
            left_steps += 1
        if i == startIndex:
            return -1
        # go right 
        i = (startIndex + 1) % n 
        right_steps = 1 
        while i != startIndex and words[i] != target:
            i += 1
            i %= n
            right_steps += 1
        return min(left_steps, right_steps)