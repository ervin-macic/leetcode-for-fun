def main():
    a = [1,4,6,7,8,9,10]
    x = 6
    l = 0
    r = len(a)
    # Invariant: a[0..l) < x <= a[r..N) where N = len(a)
    while l < r:
        m = (r-l)//2 + l
        if a[m] < x:
            l = m + 1
        elif a[m] >= x:
            r = m
    
    print(r)

main()