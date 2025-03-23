while True:
    n1 = int(input("Enter 1st number: "))
    n2 = int(input("Enter 2nd number: "))
    m = n1 if n1<n2 else n2
    n = n1 if n1>n2 else n2
    armstongs = []
    for i in range(m, n+1):
        pow = len(str(i))
        ori = i
        sum = 0
        while(ori):
            digi = ori%10
            sum += digi**pow
            ori = int(ori/10)
        if(sum==i):
            armstongs.append(i)
    if armstongs:
        print(f"Armstrong numbers between {n1} and {n2} are: {armstongs}")
    else:
        print("No Armstrong number found")


