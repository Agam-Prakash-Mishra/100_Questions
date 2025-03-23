while True:
    bin = int(input("Enter a binary number: "))
    dec = 0
    base = 1;
    while bin:
        digi = bin % 10
        bin //= 10
        dec = dec + digi*base;
    print(f"Decimal equivalent: {dec}")