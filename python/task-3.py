# Multi-Branch Retail Inventory Transfer

# Stock available at each branch
stock = {
    "Branch A": {"Laptop": 20, "Mobile": 10, "Tablet": 15},
    "Branch B": {"Laptop": 5, "Mobile": 25, "Tablet": 8},
    "Branch C": {"Laptop": 10, "Mobile": 5, "Tablet": 20}
}

# Target stock for each branch
target = {
    "Branch A": {"Laptop": 15, "Mobile": 15, "Tablet": 10},
    "Branch B": {"Laptop": 12, "Mobile": 15, "Tablet": 12},
    "Branch C": {"Laptop": 8, "Mobile": 10, "Tablet": 15}
}

surplus = {}
shortage = {}

print("RETAIL INVENTORY TRANSFER")
print("-------------------------")

# Calculate surplus and shortage
for branch in stock:
    surplus[branch] = {}
    shortage[branch] = {}

    for item in stock[branch]:
        difference = stock[branch][item] - target[branch][item]

        if difference > 0:
            surplus[branch][item] = difference
        elif difference < 0:
            shortage[branch][item] = -difference

# Display surplus
print("\nSURPLUS STOCK")

for branch in surplus:
    for item, quantity in surplus[branch].items():
        print(branch, "-", item, ":", quantity)

# Display shortage
print("\nSHORTAGE STOCK")

for branch in shortage:
    for item, quantity in shortage[branch].items():
        print(branch, "-", item, ":", quantity)

# Generate transfers
print("\nSUGGESTED TRANSFERS")

for item in ["Laptop", "Mobile", "Tablet"]:
    for receiver in stock:
        if item not in shortage[receiver]:
            continue

        for donor in stock:
            if item not in surplus[donor]:
                continue

            if receiver == donor:
                continue

            quantity = min(
                shortage[receiver][item],
                surplus[donor][item]
            )

            if quantity > 0:
                print(
                    quantity, item, "from", donor,
                    "to", receiver
                )

                shortage[receiver][item] -= quantity
                surplus[donor][item] -= quantity