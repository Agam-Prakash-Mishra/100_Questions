while True:
    n = int(input("Enter a natural num: "))
    if n<1:
        continue
    else:
        print(f"Sum of {n} Natural nums: {n*(n+1)/2}")