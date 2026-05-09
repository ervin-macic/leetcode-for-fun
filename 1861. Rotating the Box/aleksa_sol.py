class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m = len(boxGrid)
        n = len(boxGrid[0])
        for i, row in enumerate(boxGrid):
            vacant_place = n - 1
            for j in range(n - 1, -1, -1):
                if row[j] == '*':
                    vacant_place = j - 1
                elif row[j] == '#':
                    row[j], row[vacant_place] = row[vacant_place], row[j]
                    vacant_place -= 1
        res = [['.'] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                res[i][j] = boxGrid[m-1-j][i]
        return res