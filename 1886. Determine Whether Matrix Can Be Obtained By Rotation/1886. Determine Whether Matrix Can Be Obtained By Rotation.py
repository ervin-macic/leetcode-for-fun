class Solution:
    def findRotation(self, mat: list[list[int]], target: list[list[int]]) -> bool:
        n = len(mat)
        
        # mat == target
        identical = (mat == target)
        
        # flip around non-main diagonal
        flip = True 
        for i in range(n):
            for j in range(n):
                if mat[i][j] != target[n-i-1][n-j-1]:
                    flip = False
                    break
            
        # 90 anticlockwise
        anticlockwise = True
        for i in range(n):
            for j in range(n):
                if mat[i][j] != target[n-j-1][i]:
                    anticlockwise = False 
                    break
        
        # 90 clockwise 
        clockwise = True 
        for i in range(n):
            for j in range(n):
                if mat[i][j] != target[j][n-i-1]:
                    clockwise = False
                    break
        return (identical or flip or clockwise or anticlockwise)
        