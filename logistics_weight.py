"""
Write a program that advises the logistics manager on how many goods the company's vehicles can accommodate based on
their dimensions. The program should ask the manager to input the length, width, and height of the vehicle in meters.
If each cubic meter can hold 100 kilograms of goods, the program should calculate and output the maximum weight
capacity of the vehicle.
Note: If the calculated weight capacity exceeds 5000 kilograms, the program should display a message indicating that
the maximum weight capacity is 5000 kilograms."""


# Ask logistics manager to input
length = float(input("Enter the length of vehicle in (m): "))
width = float(input("Enter the width of vehicle in (m): "))
height = float(input("Enter the height of vehicle in (m): "))

# Finding the volume of the vehicle  in (m^3)
cubic_meter = length * width * height

# Calculating max weight capacity of the vehicle in (kg)

capacity = cubic_meter * 100

if capacity > 5000:
    print("Maximum weight capacity is 5000kgs")
else:
    print(f"The maximum weight capacity of this vehicle is {capacity} kgs")




