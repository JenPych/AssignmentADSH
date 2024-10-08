'''Write a program that generates a delivery schedule for the company's drivers. The program should ask the user to
input the name of 3 drivers and their license number (in a prescribed and acceptable format). The program should then
ask to enter the number of delivery available and then display assigned number of deliveries of each driver,
ensuring that each driver has an equal number of deliveries except the last one who can have more than others if needed.
'''


driver_a = str(input("Enter the name of 1st driver: "))
license_a = str(input("Enter the driver's license number: "))
driver_b = str(input("Enter the name of 2nd driver: "))
license_b = str(input("Enter the driver's license number: "))
driver_c = str(input("Enter the name of 3rd driver: "))
license_c = str(input("Enter the driver's license number: "))

# Store driver information as tuples (name, license)
driver_info = [(driver_a, license_a), (driver_b, license_b), (driver_c, license_c)]

# Get number of deliveries
number_deliveries = int(input("Enter the number of deliveries: "))

# Calculate the basic deliveries per driver and remainder
deliveries_per_driver = number_deliveries // 3  # Divide equally
remaining_deliveries = number_deliveries % 3    # Remainder goes to the last driver

# Assign deliveries to each driver
driver_a_deliveries = deliveries_per_driver
driver_b_deliveries = deliveries_per_driver
driver_c_deliveries = deliveries_per_driver + remaining_deliveries  # Last driver gets the remainder

# Display the delivery assignments
print(f"{driver_info[0][0]} ({driver_info[0][1]}) has {driver_a_deliveries} deliveries.")
print(f"{driver_info[1][0]} ({driver_info[1][1]}) has {driver_b_deliveries} deliveries.")
print(f"{driver_info[2][0]} ({driver_info[2][1]}) has {driver_c_deliveries} deliveries.")
