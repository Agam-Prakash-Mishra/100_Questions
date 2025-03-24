while True:#12001
    n = int(input("Enter a number: "))
    base = 10
    pow = 0
    newNum = 0
    while n:
        rem = n%10
        if rem ==0:
            newNum = newNum + base**pow
            pow += 1
        else:
            newNum = newNum + rem*base**pow
            pow += 1
        n = n//base
    print(f"The required number is: {newNum}")