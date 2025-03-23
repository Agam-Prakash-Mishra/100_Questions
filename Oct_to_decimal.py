while True:
    oct = int(input("Enter an octal number: "))
    base = 1
    dec = 0
    while oct:
        rem = oct % 10
        dec = dec + (rem * base)
        base = base * 8
        oct = oct // 10
    print("Decimal equivalent is:", dec)