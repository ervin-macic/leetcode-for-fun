class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        freq = [0] * (max(asteroids) + 1)
        for a in asteroids:
            freq[a] += 1
        for i, f in enumerate(freq):
            if mass < i:
                return False 
            mass += i * f 
        return True 
            