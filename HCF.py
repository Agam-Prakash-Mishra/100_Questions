while True:
    n1 = int(input("Enter 1st number: "))
    n2 = int(input("Enter 2nd number: "))
    m = n1 if n1 < n2 else n2
    n2 = n1 if n1 > n2 else n2
    for i in range(m,  0, -1):
        if n2 % i == 0 and n1 % i == 0:
            print(f"HCF of {n1} and {n2} is {i}")


