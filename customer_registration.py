"""
Create a program that allows customers to enter their details to create a new account. Each customer should be asked
to input the following information:

a. Customer's name
b. Mobile number
c. Address
d. Email address
e. Date of Birth

The program should validate the entered details and store them securely (Using appropriate Data Structure). If the
user registration is successful (based on age is more than 21 and mobile number is 10 digit), display a success
message with all the entered details; otherwise, display an appropriate error message.
"""

from datetime import datetime


def name_verify(name):
    if any(char.isdigit() for char in name):
        return False
    return True


def mobile_verify(mobile):
    return len(mobile) == 10 and mobile.isdigit()


def email_verify(email):
    if "@" and ".com" not in email:
        return False
    return True


def dob_verify(dob):
    try:
        date = datetime.strptime(dob, "%d/%m/%Y")
        today = datetime.today()
        age = today.year - date.year - ((today.month, today.day) < (date.month, date.day))
        # This checks if the current date (
        # month and day) is before the birthday (month and day). If it is, this expression evaluates to True (which
        # is equivalent to 1 in arithmetic), and subtracts one from the age. If it's not before the birthday,
        # it evaluates to False (or 0), and no adjustment is made.
        return age
    except ValueError:
        print("Error: Invalid date format. Please use dd/mm/yyyy.")
        return -1  # Indicate an invalid date


def store_customer_data(customers, name, mobile, address, email, dob):
    """Stores the customer details in a dictionary."""
    customer_id = 1000 + len(customers) + 1
    customers[customer_id] = {
        "Name": name,
        "Mobile": mobile,
        "Address": address,
        "Email": email,
        "DOB": dob
    }
    return customer_id


if __name__ == "__main__":
    customers = {}  # Dictionary to store customer data

    name, mobile, address, email, dob = None, None, None, None, None

    while True:
        if name is None:
            name = input("Enter your Full Name: ")
            if not name_verify(name):
                print("Error: Name should not contain numbers.")
                name = None
                continue

        if mobile is None:
            mobile = input("Enter your Mobile Number: ")
            if not mobile_verify(mobile):
                print("Error: Mobile number should be 10 digits.")
                mobile = None
                continue

        if address is None:
            address = input("Enter your Permanent Address: ")

        if email is None:
            email = input("Enter your E-mail Address: ")
            if not email_verify(email):
                print("Error: Incorrect e-mail address entered.")
                email = None
                continue

        if dob is None:
            dob = input("Enter your Date of Birth dd/mm/yyyy: ")
            age = dob_verify(dob)
            if age == -1:
                dob = None
                continue
            if age < 21:
                print("Error: Age should be at least 21 years old.")
                dob = None
                continue

        # Confirm details with user
        print("\n--- Confirm Your Details ---")
        print(f"Name: {name}")
        print(f"Mobile Number: {mobile}")
        print(f"Permanent Address: {address}")
        print(f"E-mail: {email}")
        print(f"Date of Birth: {dob}")

        confirm = input("Is the above details correct? (Y/N): ").upper()
        if confirm == "Y":
            customer_id = store_customer_data(customers, name, mobile, address, email, dob)
            print("\nRegistration Successful!")
            print(f"Your unique Customer ID is: {customer_id}. Please keep it safe.")
            break
        else:
            # Reset any fields user wants to change
            reset_field = input("Which field would you like to modify? (Name/Mobile/Address/Email/DOB): ").lower()
            if reset_field == "name":
                name = None
            elif reset_field == "mobile":
                mobile = None
            elif reset_field == "address":
                address = None
            elif reset_field == "email":
                email = None
            elif reset_field == "dob":
                dob = None
            continue
