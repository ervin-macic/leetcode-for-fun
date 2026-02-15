class Solution:
    def addBinary(self, a: str, b: str) -> str:
        la = len(a)
        lb = len(b)
        if la > lb:
            a, b = b, a
            la, lb = lb, la
        zero_prefix = '0' * (lb-la)
        a = zero_prefix + a
        ans = [' '] * lb
        i = lb-1
        carry = 0
        while i >= 0:
            if carry:
                if a[i] == b[i] == '1':
                    ans[i] = '1'
                elif a[i] == b[i] == '0':
                    ans[i] = '1'
                    carry = 0 
                else:
                    ans[i] = '0'
            else:
                if a[i] == b[i] == '1':
                    ans[i] = '0'
                    carry = 1
                elif a[i] == b[i] == '0':
                    ans[i] = '0'
                else:
                    ans[i] = '1'
            i -= 1
        if carry:
            ans = ['1'] + ans 
        ans = ''.join(ans)
        return ans 

sol = Solution()
a = "1111"
b = "1111"
print(sol.addBinary(a, b))



                