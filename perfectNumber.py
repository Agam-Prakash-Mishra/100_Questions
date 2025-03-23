while True:
    n = int(input("Enter a number: "))
    if n > 0:
        sum = 0
        for i in range(1, n):
            if n%i == 0:
                sum += i
        if sum == n:
            print(f"{n} is a perfect number")

