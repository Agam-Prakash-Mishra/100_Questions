while True:
    oct = input("Enter an octal number: ")
    oct_to_bin = {0: "000", 1: "001", 2: "010", 3: "011", 4: "100", 5: "101", 6: "110", 7: "111"}
    bin = ""
    while oct:
        bin = oct_to_bin[int(i)] + bin
        oct = oct[: -1]
    print(f"Binary equivalent: {bin}")