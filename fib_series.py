while True:
    def fib(n):
        if n<=1:
            return n
        else:
            return fib(n-1) + fib(n-2)
    n = int(input("Enter a number: "))
    for i in range(0,n+1):
        print(fib(i), end=" ")
    print()
        
        