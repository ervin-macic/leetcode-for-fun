# Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
# Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
from collections import defaultdict

def are_anagrams(a : str, b : str) -> bool: # This is O(nlogn) 
    if len(a) != len(b):
        return False
    a = sorted(a)
    b = sorted(b)
    i = 0
    while i < len(a):
        if a[i] != b[i]:
            return False
        i += 1
    return True

def fast_are_anagrams(a: str, b: str) -> bool: # This is O(n) but O(n) space also
    if len(a) != len(b):
        return False
    a_count = defaultdict(int)
    b_count = defaultdict(int)

    s = []
    for i in range(len(a)):
        s.append(a[i])
        s.append(b[i])
        a_count[a[i]] += 1
        b_count[b[i]] += 1

    for ch in s:
        if a_count[ch] != b_count[ch]:
            return False
    return True

def main():
    a = "eat"
    b = "ant"
    c = "ate"
    print(fast_are_anagrams(a,b))
    print(fast_are_anagrams(a,c))
    groups = defaultdict(list)
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    for word in words:
        sorted_word = str(sorted(word))
        groups[sorted_word].append(word)

    print(list(groups.values()))

main()