while True:
    n = input("Enter a number: ")
    pow = len(n)
    n= int(n)
    m=n
    arm = 0
    while(n):
        digi = n%10
        n = n//10
        arm += digi**pow
    if(arm == m):
        print("Armstrong number")
    else:
        print("Not Armstrong number")
        
