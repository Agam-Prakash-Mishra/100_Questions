while True:
    bin = input("Enter a binary number: ")
    bin_to_oct = {0: '0', 1: '1', 10: '2', 11: '3', 100: '4', 101: '5', 110: '6', 111: '7'}
    octal = ""
    while bin:
        octal = bin_to_oct[int(bin[-3:])] + octal
        # bin = str(int(int(bin)/1000))⭐ why it will not work...?
        bin = bin[:-3]
    print(f"The octal equivalent of {bin} is {octal}")