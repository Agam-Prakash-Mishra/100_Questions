
n = int(input("Enter a number: "))
len = len(str(n))
if n > 0:
    if (str(n*n))[-len:] == str(n):
        print(f"{n} is a automorphic number")
