while True:
    def fact(n):
        if n == 0:
            return 1
        else:
            return n * fact(n - 1)
    ppl = int(input("Enter the number of people: "))
    seats = int(input("Enter the number of seats: "))
    if ppl >= seats:
        p = fact(ppl) // fact(ppl - seats)
        print(f"The number of ways to seat {ppl} people is {p}")