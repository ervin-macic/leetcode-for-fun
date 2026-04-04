class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        cols = len(encodedText) // rows
        result = []
        for d in range(cols):
            for i in range(rows):
                j = i + d
                if j < cols:
                    result.append(encodedText[j + i * cols])
        return "".join(result).rstrip()

sol = Solution()
encodedText = "iveo    eed   l te   olc"
rows = 4
print(sol.decodeCiphertext(encodedText, rows))