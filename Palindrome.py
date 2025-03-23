while True:
    n = int(input("Enter a number: "))
    m = n
    rev = 1
    while m > 0:
        last_digit = m % 10
        m = m // 10
        rev = rev * 10 + last_digit
    if rev == n:
        print(f"{n} is a palindrome")
