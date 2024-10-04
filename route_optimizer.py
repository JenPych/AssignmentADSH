"""Write a program that optimizes the delivery routes for multiple destinations. The program should ask the user to
input the Name of 3 destinations and the distances to each destination from the warehouse in kilometres. Using this
information, the program should design the route such that the driver visits all destinations based on the distance
in a descending order( i.e. starting with the longest delivery first) and return to the starting point. The program
should then display the optimized route.
Note: If 2 destinations have same distance then it must prioritize the destination that has been entered first."""

# Ask the user to input names of destination
dest_a = str(input("Enter the name of 1st destination: "))
distance_a = float(input("Enter the distance of 1st destination in (km): "))
dest_b = str(input("Enter the name of 2nd destination: "))
distance_b = float(input("Enter the distance of 2nd destination in (km): "))
dest_c = str(input("Enter the name of 3rd destination: "))
distance_c = float(input("Enter the distance of 3rd destination in (km): "))

# create a list and store dest with their respective distance
destination = [(dest_a, distance_a), (dest_b, distance_b), (dest_c, distance_c)]

# Sort destinations by distance in descending order
optimized_route = sorted(destination, key=lambda x: x[1], reverse=True)

# Display the optimized route
print("\n--- Optimized Delivery Route ---")
for i, (destination, distance) in enumerate(optimized_route, 1):
    print(f"Stop {i}: {destination} ({distance} km)")

print("Return to the warehouse.")



