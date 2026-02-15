class Solution:
    def addStrings(self, a: str, b: str) -> str:
        la = len(a)
        lb = len(b)
        if la > lb:
            a, b = b, a
            la, lb = lb, la
        zero_prefix = '0' * (lb-la)
        a = zero_prefix + a
        a = ''.join(a)
        ans = [' '] * lb
        i = lb-1
        carry = 0
        while i >= 0:
            ai = ord(a[i]) - ord('0')
            bi = ord(b[i]) - ord('0')
            s = ai + bi
            if carry:
                s += 1
                if s > 9:
                    ans[i] = str(s % 10)
                else:
                    ans[i] = str(s)
                    carry = 0
            else:
                if s > 9:
                    ans[i] = str(s % 10)
                    carry = 1
                else:
                    ans[i] = str(s)
            i -= 1
        if carry:
            ans = ['1'] + ans 
        ans = ''.join(ans)
        return ans 

sol = Solution()
a = "3589"
b = "9735448"
print(sol.addBinary(a, b))



                