while True:
    dec = int(input("Enter a decimal number: "))
    bin = ""
    while dec:
        bin = str(dec % 2) + bin
        dec = dec // 2
    print(f"Binary representation of {dec} is {bin}")