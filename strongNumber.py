while True:
    def fact(n):
        if n==0:
            return 1
        else:
            return n*fact(n-1)
    n = int(input("Enter a number: "))
    if n>=0:
        sum = 0
        m = n
        while m:
            rem = m%10
            sum += fact(rem)
            m = m//10
        if sum==n:
            print(f"{n} is a strong number")
        else:
            print(f"{n} is not a strong number")
        