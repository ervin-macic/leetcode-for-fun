def main():
    a = [3,5,-16,3,6,-3,7,-5]
    
    best_so_far = 0
    best_here = 0
    for i in range(len(a)):
        best_here = max(a[i]+best_here, 0)
        best_so_far = max(best_here, best_so_far)
        
    
    print(best_so_far)

main()