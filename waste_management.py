# AI Based Waste Management System

waste_data = []

def show_menu():
    print("\n===== AI Waste Management System =====")
    print("1. Add Waste")
    print("2. View Records")
    print("3. Recycling Suggestion")
    print("4. Waste Statistics")
    print("5. Save Records")
    print("6. Exit")

def classify_waste(waste):
    waste = waste.lower()
    categories = {
        "plastic": "Blue Bin",
        "paper": "Blue Bin",
        "glass": "Green Bin",
        "metal": "Grey Bin",
        "organic": "Brown Bin",
        "ewaste": "Red Bin"
    }
    return categories.get(waste, "Unknown")

def recycling_tip(waste):
    tips = {
        "plastic": "Recycle into new plastic products.",
        "paper": "Recycle into notebooks or cartons.",
        "glass": "Clean and recycle glass bottles.",
        "metal": "Recycle metal cans and scraps.",
        "organic": "Convert into compost.",
        "ewaste": "Give to authorized e-waste centers."
    }
    return tips.get(waste.lower(), "No suggestion available.")

def add_waste():
    waste = input("Enter Waste Type: ")
    weight = float(input("Enter Weight (kg): "))
    bin_name = classify_waste(waste)
    waste_data.append({
        "type": waste,
        "weight": weight,
        "bin": bin_name
    })
    print("Waste Added Successfully!")
    print("Suggested Bin:", bin_name)

def view_records():
    if not waste_data:
        print("No records found.")
        return
    print("\nWaste Records")
    for i, item in enumerate(waste_data, start=1):
        print(i, item["type"], "-", item["weight"], "kg", "-", item["bin"])

def show_statistics():
    total_weight = 0
    for item in waste_data:
        total_weight += item["weight"]
    print("Total Waste Records:", len(waste_data))
    print("Total Weight:", total_weight, "kg")

def save_records():
    file = open("waste_records.txt", "w")
    for item in waste_data:
        file.write(
            item["type"] + "," +
            str(item["weight"]) + "," +
            item["bin"] + "\n"
        )
    file.close()
    print("Records Saved Successfully!")

while True:
    show_menu()
    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_waste()

    elif choice == "2":
        view_records()

    elif choice == "3":
        waste = input("Enter Waste Type: ")
        print(recycling_tip(waste))

    elif choice == "4":
        show_statistics()

    elif choice == "5":
        save_records()

    elif choice == "6":
        print("Thank You for Using AI Waste Management System!")
        break

    else:
        print("Invalid Choice! Please Try Again.")
