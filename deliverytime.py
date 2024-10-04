"""Write a program that estimates the delivery time for a given route. The program should ask the user to input the
distance of the route in kilometres and the average speed of the delivery vehicle in kilometres per hour. Using this
information, the program should calculate and display the estimated delivery time in hours.
Note: If the calculated estimated delivery time is more than 15 hours, your code should take into account the driver
rest time. Your program should add 8 hours rest to the delivery time and print the total estimated delivery time
accordingly."""


# Ask the user to input
distance = float(input("Enter the distance of delivery in (km): "))
avg_speed = float(input("Enter the average speed of delivery vehicle in (km/h): "))

# Finding the estimated delivery time
delivery_time = distance / avg_speed

# In condition that delivery time is more than 15 hours
if delivery_time >= 15:
    delivery_time += 8

print(f"Total estimated delivery time = {delivery_time} hrs")
