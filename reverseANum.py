while True:
    n = int(input("Enter a number: "))
    rev  = 1
    while(n):
        digi = abs(n)%10
        n = int(n)/10
        rev = rev*10 + digi
    print(rev)