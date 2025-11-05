from sortedcontainers import SortedList
from collections import Counter

class Ref:
    def __init__(self, val=0):
        self.val = val

class Solution:
    def findXSum(self, nums: list[int], k: int, x: int) -> list[int]:
        n = len(nums)
        init_freq = Counter(nums[:k])

        freq = SortedList((f, v) for v, f in init_freq.items())
        count = dict(init_freq)

        top = SortedList(freq[-x:])       
        rest = SortedList(freq[:-x])  

        x_sum = 0
        for (f, v) in top:
            x_sum += f*v 
        x_sum = Ref(x_sum)
        ans = [x_sum.val]

        def rebalance(x_sum_ref):
            # ensure top has exactly x largest elements
            while len(top) > x:
                f, v = top.pop(0)
                rest.add((f, v))
                x_sum_ref.val -= f * v

            while len(top) < x and rest:
                f, v = rest.pop(-1)
                top.add((f, v))
                x_sum_ref.val += f * v

            # fix order violations
            while rest and top and rest[-1] > top[0]:
                fr, vr = rest.pop(-1)
                ft, vt = top.pop(0)
                x_sum_ref.val += fr * vr - ft * vt
                top.add((fr, vr))
                rest.add((ft, vt))

        def remove_pair(x_sum_ref, pair):
            if pair in top:
                top.remove(pair)
                x_sum_ref.val -= pair[0] * pair[1]
            else:
                rest.remove(pair)
            rebalance(x_sum_ref)

        def add_pair(x_sum_ref, pair):
            rest.add(pair)
            rebalance(x_sum_ref)

        for i in range(1, n - k + 1):
            old_elem = nums[i - 1]
            new_elem = nums[i + k - 1]
            if old_elem != new_elem:
                # Remove old element
                f_old = count[old_elem]
                remove_pair(x_sum, (f_old, old_elem))
                if f_old > 1:
                    f_old -= 1
                    add_pair(x_sum, (f_old, old_elem))
                    count[old_elem] = f_old
                else:
                    del count[old_elem]

                # Add new element
                if new_elem in count:
                    f_new = count[new_elem]
                    remove_pair(x_sum, (f_new, new_elem))
                    f_new += 1
                    add_pair(x_sum, (f_new, new_elem))
                    count[new_elem] = f_new
                else:
                    add_pair(x_sum, (1, new_elem))
                    count[new_elem] = 1

            ans.append(x_sum.val)

        return ans


sol = Solution()
nums = [1,1,2,2,3,4,2,3]
k = 6
x = 2
print(sol.findXSum(nums, k, x))  

nums1 = [2,1,3,4,3]
k = 1
x = 1
print(sol.findXSum(nums1, k, x))
