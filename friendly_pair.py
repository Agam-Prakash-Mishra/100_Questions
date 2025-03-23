while True:
    def job(n):
        sum =0
        for i in range(1,n):
            if n%i==0:
                sum = sum + i
        return sum/n;
    m = int(input("Enter 1st number: "))
    n = int(input("Enter 2nd number: "))
    if job(m) == job(n):
        print(f"{m} and {n} are friendly numbers")
    else:
        print(f"{m} and {n} are not friendly numbers")

