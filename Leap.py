while True:
    yr = int(input("Enter year"))
    if not yr%400 or yr%4==0:
        print("Leap year")
    else: 
        print("Not leap year")