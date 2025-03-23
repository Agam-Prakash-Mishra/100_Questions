while True:
    dec = int(input("Enter a decimal number: "))
    hex = ""
    while dec:
        rem = dec % 16
        if rem>9:
            hex = chr(rem + 55) + hex
        else:
            hex = str(rem) + hex
        dec //= 16
    print("Hexadecimal representation:", hex)
