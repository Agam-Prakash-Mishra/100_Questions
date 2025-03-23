while True:
    n = int(input("Enter a number: "))
    sum = 0
    m = n
    while m:
        digi = m % 10
        sum += digi
        m = m // 10
    if sum>n:
        print(f"{n} is abundant number")
