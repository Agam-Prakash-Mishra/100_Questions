while True:
    n = int(input("Enter a number: "))
    flag = 0
    if n>3:
        f=0
        prime = []
        for i in range(2, n):
            for j in range(2, i):
                if (i % j) == 0:
                    f = 1
                    break
            if f == 0:
                prime.append(i)
        
        for i in prime:
            for j in prime:
                if (i+j) == n:
                    flag = 1
                    break
        if flag == 1:
            print("Yes, there exist two prime numbers that sum up to", n)
        else:
            print("No, there do not exist two prime numbers that sum up to", n)

                