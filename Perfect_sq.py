while True:
    n = int(input("Enter a number: "))
    if n > 0:
        if (n**.5 * int(n**.5)) == n:
            print(f"{n} is a perfect square")
        else:
            print(f"{n} is not a perfect square")