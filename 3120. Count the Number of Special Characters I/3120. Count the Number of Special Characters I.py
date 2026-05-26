class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lowerCase = [False] * 26
        upperCase = [False] * 26
        for c in word:
            x = ord(c)
            if x < 97: # uppercase
                upperCase[x-65] = True 
            else:
                lowerCase[x-97] = True 
        ans = 0
        for i in range(26):
            if lowerCase[i] and upperCase[i]:
                ans += 1
        return ans
