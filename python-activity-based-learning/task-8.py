# Student Group Formation with Score Balancing

# Student names and scores
students = [
    ("Ravi", 90),
    ("Sita", 85),
    ("Arun", 80),
    ("Priya", 75),
    ("Kiran", 70),
    ("Meena", 65),
    ("Rahul", 60),
    ("Divya", 55)
]

# Number of students in each group
group_size = 2

# Sort students by score in descending order
students.sort(key=lambda x: x[1], reverse=True)

# Create empty groups and their total scores
groups = []
group_totals = []

for i in range(0, len(students), group_size):
    group = students[i:i + group_size]
    groups.append(group)
    group_totals.append(sum(student[1] for student in group))

print("STUDENT GROUP FORMATION")
print("-----------------------")

for i in range(len(groups)):
    print("\nGroup", i + 1)

    for student in groups[i]:
        print(student[0], "- Score:", student[1])

    print("Group Total Score:", group_totals[i])

# Calculate difference between highest and lowest group totals
if group_totals:
    difference = max(group_totals) - min(group_totals)

    print("\nHIGHEST GROUP TOTAL:", max(group_totals))
    print("LOWEST GROUP TOTAL:", min(group_totals))
    print("Difference Between Group Totals:", difference)

# Check whether all students are allocated
allocated_students = sum(len(group) for group in groups)

print("\nTotal Students:", len(students))
print("Allocated Students:", allocated_students)

if allocated_students == len(students):
    print("All students are allocated successfully")
else:
    print("Some students are not allocated")