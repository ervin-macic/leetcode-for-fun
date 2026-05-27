class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lowerCase = [-1] * 26
        upperCase = [-1] * 26
        for i, c in enumerate(word):
            x = ord(c)
            if x < 97: # uppercase
                if upperCase[x-65] == -1:
                    upperCase[x-65] = i
            else:
                lowerCase[x-97] = i 
        ans = 0
        for i in range(26):
            if lowerCase[i] != -1 and upperCase[i] != -1 and lowerCase[i] < upperCase[i]:
                ans += 1
        return ans
