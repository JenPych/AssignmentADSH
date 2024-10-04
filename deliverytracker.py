"""Write a program that tracks the delivery status of a package. The program should ask the user to input the
package's tracking number and display the current status of the package, such as "In transit," "Out for delivery,
" or "Delivered."
Note: Use list to store and access the data for some sample tracking (A00001D) numbers and their status "In transit,
" "Out for delivery," or "Delivered." .
Note:
The program must ask the example of tracking number acceptable for checking the status.
The Program must reply with an appropriate message if the tracking number is not in the records or invalid format."""

item_data = [('A00001D', 'In Tranzit'), ('A00009K', 'Out for Delivery'), ('A00005G', 'Delivered')]

ask_track_number = input("Enter the 7 character delivery tracking number starting with (A0*****): ").upper()

if len(ask_track_number) != 7:
    print("Invalid tracking number entered")

else:

    found = False

    for (number, status) in item_data:
        if ask_track_number == number:
            print(f"Tracking number: {ask_track_number}")
            print(f"Current Status: {status}")
            found = True
            break

    if not found:
        print("Tracking number not found in records.")


