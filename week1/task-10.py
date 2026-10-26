# Weekly Electricity Consumption Matrix

appliances = ["Fan", "AC", "Refrigerator"]
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# Electricity consumption in units (kWh)
# Each row represents an appliance
consumption = [
    [2, 2, 2, 2, 2, 3, 3],
    [8, 9, 10, 8, 9, 12, 11],
    [4, 4, 4, 4, 4, 4, 4]
]

limit = 60

print("WEEKLY ELECTRICITY CONSUMPTION")
print("------------------------------")

# Calculate total consumption for each appliance
print("\nAPPLIANCE-WISE TOTALS")

for i in range(len(appliances)):
    total = sum(consumption[i])

    print(appliances[i], ":", total, "units")

    if total > limit:
        print("Warning: Consumption exceeds limit")

# Calculate daily totals
print("\nDAILY TOTALS")

for j in range(len(days)):
    daily_total = 0

    for i in range(len(appliances)):
        daily_total += consumption[i][j]

    print(days[j], ":", daily_total, "units")

# Calculate total weekly consumption
weekly_total = 0

for i in range(len(appliances)):
    weekly_total += sum(consumption[i])

print("\nTOTAL WEEKLY CONSUMPTION:", weekly_total, "units")
