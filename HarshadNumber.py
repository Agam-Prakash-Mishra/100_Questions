while True:
    n = int(input("Enter a number: "))
    if n > 0:
        ori = n
        sum = 0
        while(ori):
            digi = ori%10
            sum += digi
            ori = int(ori/10)
        if n%sum == 0:
            print(f"{n} is a Harshad number")
