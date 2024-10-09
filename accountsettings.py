'''Implement a program that allows users to manage their account settings. Provide options to update their personal
information (e.g., name, email address, password) and communication preferences (e.g., subscription to newsletters,
promotional emails).

Note: Assume the account information are name, email address and password. The program saved the customer details in
three list. A list comprises the names, another the email addresses and the third has the passwords. If a user has
his name at position x in the first list, his email address will be found at the same position in the second lit and
his password will be also saved in the same position in the third list. Write a program that takes as input the user’
email address and password to validate and then enable the user to update personal information (email address must be
unique) and communication preferences.
'''

name = ["Aadesh Shrestha", "Yaju Shrestha", "Pratik Shrestha"]
email = ["aadesh.shrestha01@gmail.com", "yaju.shrestha02@yahoo.com", "pratik.shrestha03@live.com"]
password = ["passmetheword1", "passmetheketchup2", "passmethedrink3"]
subscription =["yes", "no", "yes"]
index = 0
# Request email
email_check = input("Enter your e-mail address: ")

# check if email exists and ask password if it exists
if email_check in email:
    index = email.index(email_check)
    password_check = input("Enter password: ")

    # Validate email and password
    if password_check == password[index]:
        print(f"Welcome to your account, {name[index]}")

        # Ask to update personal data
        ask = input("Would you like to update your personal information? Yes/No: ").lower().strip()

        if ask == "yes":
            new_name = input("Enter you name: ")
            name[index] = new_name  # update name with new name

            new_email = input("Enter your new e-mail address: ")
            if new_email in email:
                print("The e-mail is already used. Please try again and enter a new e-mail address :")
            else:
                email[index] = new_email  # update email with new unique email

                old_password = input("Enter old password: ")
                if old_password in password[index]:  # checking for old password to confirm user
                    new_password = input("Enter new password: ")
                    password[index] = new_password  # update password with new one

                    print("Your details have been updated.")
                else:
                    print(
                        "The password you entered did not match with the old password. Enter the old password again to "
                        "update your password.")

        ask_sub = input(
            "Would you like to subscribe to our newsletters and promotional emails? Yes/No: ").lower().strip()

        if ask_sub == "yes":
            subscription[index] = "yes"
            print(f"Subscription preference updated. See you again {name[index]}")
        else:
            subscription[index] = "no"
            print(f"See you again {name[index]}")

    else:
        print("The password you entered is incorrect. Try again!")

else:
    print("This e-mail address does not exist in our database. Make sure you entered your details correctly. Bye!")
