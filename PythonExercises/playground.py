def main():
    for i, x in enumerate([x*x for x in range(10)]):
        print(i, x)
    
    print(list(reversed(range(1,10))))
main()