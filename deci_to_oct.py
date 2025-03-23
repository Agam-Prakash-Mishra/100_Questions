while True:
    dec = int(input("Enter a decimal number: "))
    oct = ""
    while dec:
        oct = str(dec%8) + oct
        dec = dec//8
    print(f"The octal equivalent is: {oct}")