while True:
    n1 = int(input("Enter the first number: "))
    n2 = int(input("Enter the second number: "))
    m = n1 if n1<n2 else n2
    n = n1 if n1>n2 else n2
    while True:
        if n%m==0:
            print(f"LCM of {n1} and {n2} is {n}")
            break
        # n += n⭐why this is not correct?
        n += m