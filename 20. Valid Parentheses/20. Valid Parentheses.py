class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1: return False
        stack = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if not ((top == '(' and c == ')') or (top == '[' and c == ']') or (top == '{' and c == '}')):
                    return False 
        return not stack