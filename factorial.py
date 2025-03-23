while True:
    def factorial(n):
        #⭐ return 1 if n==0 else n*factorial(n-1)
        if n==0:
            return 1
        else:
            return n*factorial(n-1)
    n = int(input("Enter a number: "))
    if n<0:
        print("Please enter a valid number")
    else:
        print(f"Factorial of {n} is {1 if n==0 else n*factorial(n-1)}")