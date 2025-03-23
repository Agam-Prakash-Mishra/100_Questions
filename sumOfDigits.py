
while True:
    n = int(input("Enter the number: "))
    sum = 0
    while(n):
        #digi = n%10 #Modulo in Py don't works as others but it works opposite
        digi = abs(n)%10;
        #n //=10 #shouldn't use it in case of negative numbers......why??
        n = int(n/10)
        sum += digi
    print(sum)