while True:
    n = int(input("Enter a number: "))
    len =0
    while(n):
        n //= 10
        len += 1
    print("Length of the number is: ", len)            