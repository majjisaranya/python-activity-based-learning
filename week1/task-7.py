# Food Waste Monitoring System

# Daily meal details: [prepared, served, leftover]
days = [
    ["Monday", 100, 80, 20],
    ["Tuesday", 120, 100, 20],
    ["Wednesday", 150, 100, 50],
    ["Thursday", 100, 90, 10],
    ["Friday", 200, 140, 60]
]

# Acceptable wastage limit
limit = 20

print("FOOD WASTE MONITORING SYSTEM")
print("----------------------------")

total_prepared = 0
total_served = 0
total_leftover = 0

for day in days:
    name = day[0]
    prepared = day[1]
    served = day[2]
    leftover = day[3]

    total_prepared += prepared
    total_served += served
    total_leftover += leftover

    wastage = (leftover / prepared) * 100

    print("\nDay:", name)
    print("Meals Prepared:", prepared)
    print("Meals Served:", served)
    print("Leftover Meals:", leftover)
    print("Wastage Percentage:", wastage, "%")

    if wastage > limit:
        print("Status: Wastage Exceeds Limit")
    else:
        print("Status: Acceptable")

print("\nWEEKLY SUMMARY")
print("Total Meals Prepared:", total_prepared)
print("Total Meals Served:", total_served)
print("Total Leftover Meals:", total_leftover)

overall_wastage = (total_leftover / total_prepared) * 100
print("Overall Wastage Percentage:", overall_wastage, "%")
