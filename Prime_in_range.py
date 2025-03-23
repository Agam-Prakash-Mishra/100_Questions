while True:
    n1 = int(input("Enter 1st number: "))
    n2 = int(input("Enter 2nd number: ")) 
    n = n1 if n1<n2 else n2
    m = n1 if n1>n2 else n2
    if n<2 and m<2:
        print("No Prime number found!")
    elif m>=2:
        prime = []
        if(n<2):#so that no extraneous iteration in case n==-12
            n=2
        for num in range(n,m+1):
            sqRt = int(num**.5)
            for i in range(2,sqRt+1):
                if num%i==0:
                    break
            else:#⭐a clever use of for-else in Python
                prime.append(num)
        if(prime):
            print(prime)
        else:
            print("No prime number is found")
        

   