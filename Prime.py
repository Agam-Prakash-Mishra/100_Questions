while True:
    n = int(input("Enter a number: "))
    if(n<2):
        print("Not Prime number")
    elif n <= 3:
        print("Prime number")
    else:
        sqRt = int(n**(1/2))
        for i in range(2,sqRt+1):
            if not n%i:
                print("Not Prime number")
                break
        else:#⭐a clever use of for-else in Python
            print("Prime number");