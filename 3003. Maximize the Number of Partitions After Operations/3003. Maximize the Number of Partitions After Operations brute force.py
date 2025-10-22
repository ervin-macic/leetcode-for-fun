from collections import defaultdict

class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        if k == 26:
            return 1

        n = len(s)
        left_mask = [0] * n
        left_duplicates = [0] * n
        left_parts = [0] * n

        mask = 0
        duplicates = 0
        parts = 1
        for i in range(n):
            bit = 1 << (ord(s[i]) - ord('a'))
            duplicates |= mask & bit
            mask |= bit
            if bin(mask).count("1") > k:
                mask = bit
                duplicates = 0
                parts += 1
            left_mask[i] = mask
            left_duplicates[i] = duplicates
            left_parts[i] = parts

        result = parts
        mask = 0
        duplicates = 0
        parts = 0

        for i in range(n - 1, -1, -1):
            bit = 1 << (ord(s[i]) - ord('a'))
            duplicates |= mask & bit
            mask |= bit

            bit_count = bin(mask).count("1")
            if bit_count > k:
                mask = bit
                duplicates = 0
                parts += 1
                bit_count = 1

            if bit_count == k:
                if ((bit & duplicates)
                    and (bit & left_duplicates[i])
                    and (bin(left_mask[i]).count("1") == k)
                    and ((left_mask[i] | mask) != (1 << 26) - 1)):
                    result = max(result, parts + left_parts[i] + 2)
                elif duplicates:
                    result = max(result, parts + left_parts[i] + 1)

        return result


            
                
sol = Solution()

print(sol.maxPartitionsAfterOperations("noyynxgvtkhxsqdqcjyecjpwcawkgsrxmixokubliztvglyftkcrkpdfofwhaydetelrlyzirwmcjlnghqzsepsztnshfsanwezyrwugjtupaukeqhnqjuuyzlixhzewymafxyjasqlfvvabungssaylgcxydwvnwcayoogevdkpkxbvofwgohtjocqhtykbrpurqxqvwyxdxxqhstlbkcuohtkmlyqfdzcbatmshcpoeoqirqtyuabiwrtyprucmfpcezmawmjhsskexpzlnasejilkjtbwuylzdpunifykhyteoglauzfaljvndlpeubkxtmnisawrdlzfcvfljdrtnzwhyuelqdtbgjvrublexxslrckupnwznerwanngvfppxnayeorsgnozapmgnsbzuxmaeoyrfwhhsdnxsflqklbtopradhxgadzjrrdutduhiurdjaovkgtulcjndpcibywdzwxucxakouievplehkdkdhpnfgjqrrjcwdnwgfujzpkihjjvxrdtluuxdpzwwgdifhzvuuhpoe", 22))