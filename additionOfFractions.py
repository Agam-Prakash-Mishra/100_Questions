while True:
    def hcf(a, b):
        while(b):
            a, b = b, a % b
        return a
    num1, den1 = map(int, input("Enter the first fraction: ").split())
    num2, den2 = map(int, input("Enter the second fraction: ").split())
    if den1 == 0 or den2 == 0:
        print("Error: Denominator cannot be zero.")
    else:
        num = (num1 * den2) + (num2 * den1)
        den = den1 * den2
        gcd = hcf(num, den)
        # hcf = lambda a, b: b if a % b == 0 else hcf(b, a % b)
        print(f"The sum of the two fractions is {num/gcd}/{den/gcd}")