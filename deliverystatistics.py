'''Create a program that calculates and displays the statistics of the company's deliveries. The program should ask
the user to input the destination of 3 deliveries and the delivery times for each delivery. Using this information,
the program should calculate and display the average delivery time and the fastest and slowest delivery times with
destinations.
'''
dest_a = str(input("Enter the name of 1st destination: "))
time_a = float(input("Enter the delivery time in (hrs): "))
dest_b = str(input("Enter the name of 2nd destination: "))
time_b = float(input("Enter the delivery time in (hrs): "))
dest_c = str(input("Enter the name of 3rd destination: "))
time_c = float(input("Enter the delivery time in (hrs): "))

delivery = [(dest_a, time_a), (dest_b, time_b), (dest_c, time_c)]

# calculate average delivery time
average = (time_a + time_b + time_c) / 3

# Initialize fastest and slowest deliveries
fastest_delivery = delivery[0]
slowest_delivery = delivery[0]

# Find fastest and slowest deliveries by iterating
for deli in delivery:
    if deli[1] < fastest_delivery[1]:
        fastest_delivery = deli
    if deli[1] > slowest_delivery[1]:
        slowest_delivery = deli

# display avg, fastest and slowest
print("The average delivery time is:", average, "hrs")
print("The fastest delivery time is:", fastest_delivery, "hrs")
print("The slowest delivery time is:", slowest_delivery, "hrs")



