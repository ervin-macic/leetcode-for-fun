from typing import List
class Node():
    def __init__(self):
        self.children = [None] * 10
        self.isLeaf = False

class Trie():
    def __init__(self):
        self.root = Node()
   
    def addWord(self, word: str):
        curr = self.root
        for c in word:
            d = int(c) # d in 0 to 9
            if not curr.children[d]:
                curr.children[d] = Node()
            curr = curr.children[d]
        curr.isLeaf = True
    
    def findMaxPrefixInTrie(self, target: str):
        curr = self.root 
        i = 0
        while i < len(target) and curr and curr.children[int(target[i])]:
            curr = curr.children[int(target[i])]
            i += 1
        return i
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        t = Trie()
        for x in arr1:
            t.addWord(str(x))
        ans = 0
        for x in arr2:
            ans = max(ans, t.findMaxPrefixInTrie(str(x)))
        return ans


sol = Solution()
arr1 = [1,10,100]
arr2 = [1000]
print(sol.longestCommonPrefix(arr1, arr2))