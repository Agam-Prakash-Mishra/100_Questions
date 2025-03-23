while True:
    n = int(input("Enter a number: "))
    a, b = 0, 1
    if n<=0:
        print("Invalid input")
    elif n==1:
        print(f"Fibonacci 1st num: {a}")
    elif n==2:
        print(f"Fibonacci 2nd num: {b}")
    else:
        for _ in range(2, n):
            a, b = b, a+b
        print(f"Fibonacci {n}th num: {b}")
