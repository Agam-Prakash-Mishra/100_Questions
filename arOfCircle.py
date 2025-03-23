from math import pi 
while True:
    r = float(input("Enter the radius of the circle: "))
    if r<0:
        print("Radius should be positive.")
    else:
        area = pi * r**2
        print(f"The area of the circle is: {area:.2f}")#⭐