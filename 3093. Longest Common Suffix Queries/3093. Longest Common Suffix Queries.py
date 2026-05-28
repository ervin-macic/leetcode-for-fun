from typing import List
class Node:
    def __init__(self):
        self.children = {}
        self.best_idx = -1
        self.best_len = float('inf')

class Trie:
    def __init__(self):
        self.root = Node()

    def update(self, node, idx, length):
        if length < node.best_len or (length == node.best_len and idx < node.best_idx):
            node.best_len = length
            node.best_idx = idx

    def addWord(self, word, idx):
        curr = self.root
        self.update(curr, idx, len(word))
        for c in reversed(word):
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
            self.update(curr, idx, len(word))

    def query(self, word):
        curr = self.root
        for c in reversed(word):
            if c not in curr.children:
                break
            curr = curr.children[c]
        return curr.best_idx

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        t = Trie()
        for i, w in enumerate(wordsContainer):
            t.addWord(w, i)
        return [t.query(q) for q in wordsQuery]