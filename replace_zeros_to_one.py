while True:#12001
    n = int(input("Enter a number: "))
    base = 10
    pow = 0
    newNum = 0
    while n:#10^0 = 1
        rem = n%10
        if rem ==0:
            newNum = newNum + base**0
            pow += 1
        else:
            newNum = newNum + rem*base**pow # 3+ 3*10^2
            pow += 1
        n = n//base
    print(f"The required number is: {newNum}")