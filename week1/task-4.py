# University Hostel Room Allocation

# Hostel rooms and their capacities
rooms = {
    "Room 101": 2,
    "Room 102": 3,
    "Room 103": 2
}

# Student details
students = [
    {"name": "Ravi", "eligible": True, "group": "A"},
    {"name": "Sita", "eligible": True, "group": "A"},
    {"name": "Arun", "eligible": True, "group": "B"},
    {"name": "Priya", "eligible": True, "group": "B"},
    {"name": "Kiran", "eligible": True, "group": "A"},
    {"name": "Meena", "eligible": False, "group": "A"},
    {"name": "Rahul", "eligible": True, "group": "C"},
    {"name": "Divya", "eligible": True, "group": "C"},
    {"name": "Ajay", "eligible": True, "group": "B"}
]

# Group restrictions for each room
allowed_groups = {
    "Room 101": ["A"],
    "Room 102": ["B", "C"],
    "Room 103": ["A", "B", "C"]
}

# Store room assignments
allocation = {room: [] for room in rooms}
assigned_students = set()
unallocated = []

print("UNIVERSITY HOSTEL ROOM ALLOCATION")
print("---------------------------------")

# Allocate students to rooms
for student in students:

    name = student["name"]
    group = student["group"]

    if not student["eligible"]:
        print(name, "- Not eligible for hostel")
        unallocated.append(name)
        continue

    allocated = False

    for room in rooms:

        if (
            len(allocation[room]) < rooms[room]
            and group in allowed_groups[room]
        ):
            allocation[room].append(name)
            assigned_students.add(name)
            allocated = True
            break

    if not allocated:
        unallocated.append(name)
        print(name, "- No suitable room available")

# Display room assignments
print("\nROOM ALLOCATION DETAILS")

for room in rooms:
    print(room, ":", allocation[room])
    print("Capacity:", rooms[room])
    print("Occupied:", len(allocation[room]))
    print("Available:", rooms[room] - len(allocation[room]))

# Check duplicate assignments
print("\nDUPLICATE ASSIGNMENT CHECK")

all_assigned = []

for room in allocation:
    all_assigned.extend(allocation[room])

duplicates = []

for name in all_assigned:
    if all_assigned.count(name) > 1 and name not in duplicates:
        duplicates.append(name)

if duplicates:
    print("Duplicate assignments:", duplicates)
else:
    print("No duplicate assignments found")

# Display unallocated students
print("\nUNALLOCATED STUDENTS:", unallocated)
print("Total unallocated:", len(unallocated))
