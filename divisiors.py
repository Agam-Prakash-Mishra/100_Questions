while True:
    n = int(input("Enter a number: "))
    if n>0:
        for i in range(1,n+1):
            if n%i==0:
                print(i, end=" ")
    print()