def countBelongings(self, intervals) -> list[int]:
        M = max([b for [a,b] in intervals])
        m = min([a for [a,b] in intervals])
        diff_arr = [0] * (M-m+2)
        for [a,b] in intervals:
            diff_arr[a-m] += 1
            diff_arr[b-m+1] -= 1
        cumsum = 0
        for (i,v) in enumerate(range(m,M+1)):
            cumsum += diff_arr[i]
            print(f"Value {v} belongs to {cumsum} intervals in total.")
        return diff_arr