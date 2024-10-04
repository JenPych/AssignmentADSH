"""Create a program that calculates and prints the total cost of a delivery based on the weight of the goods and the
delivery distance. The program should ask the user to input the weight of the goods in kilograms and the delivery
distance in kilometres. The cost per kilometre is $0.10 per kilogram. The minimum delivery charges are $30 and the
program should apply a 5% discount for deliveries over 100 kilometres. The program should then calculate and display
the total cost of the delivery.
Note: The program must roundoff the weight to the nearest positive value before calculating the cost of delivery."""


# Ask the user to input
weight = float(input("Enter the weight of goods for delivery in (kgs): "))
del_distance = float(input("Enter the distance of delivery in (km): "))

# round-off the weight to the nearest positive value
weight = round(weight)

# Finding the estimated delivery cost in ($)
delivery_cost = (0.10 * weight) * del_distance

# Finding total cost after applying minimum charges and discount
if del_distance >= 100:
    actual_delivery_cost = 30 + (delivery_cost - (0.05 * delivery_cost))  # discount

else:
    actual_delivery_cost = 30 + delivery_cost  # no discount

print(f"Total delivery cost = ${actual_delivery_cost}")

