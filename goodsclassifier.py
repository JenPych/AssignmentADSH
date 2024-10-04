"""Create a program that classifies goods into different categories based on their weight. The program should ask the
user to insert the weight of a goods item in pounds. Based on the weight, the program should categorize the goods as
follows:
• Lightweight: Less than 10 kilograms
• Mediumweight: More than 10 to 50 kilograms
• Heavyweight: More than 50 kilograms to 120 Kilograms
• Must be divided in small sizes: More than 120 Kilograms
The program should then display the category of the goods.
"""

# Ask the user to input the goods name and their weight
item = str(input("Enter the name of goods: "))
weight = float(input("Enter the weight of the goods in (kgs): "))
category = ()
item_details = {"name": item, "weight": weight}


if weight < 10:
    print(f"The {item} is/are Light weight.")
    category = "Lightweight"

if 10 <= weight < 50:
    print(f"The {item} is/are Medium weight.")
    category = "Medium weight"

if 50 <= weight <= 120:
    print(f"The {item} is/are Heavy weight.")
    category = "Heavy weight"

if weight > 120:
    print(f"The {item} should be divided into small sizes as 1 item cannot exceed 120 kgs")
    category = "Item should be divided."


item_details["category"] = category

# Display the details
print(f"\nItem details:")
for key, value in item_details.items():
    print(f"{key.capitalize()}: {value}")

