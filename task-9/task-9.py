# Student Marks Matrix Analysis

students = ["Ravi", "Sita", "Arun", "Priya"]
subjects = ["Python", "Maths", "English"]

# Marks of students in different subjects
marks = [
    [85, 90, 78],
    [92, 88, 95],
    [65, 70, 60],
    [75, 80, 72]
]

print("STUDENT MARKS MATRIX ANALYSIS")
print("-----------------------------")

# Calculate student-wise totals and averages
totals = []

for i in range(len(students)):
    total = sum(marks[i])
    average = total / len(subjects)
    totals.append(total)

    print("\nStudent:", students[i])
    print("Total Marks:", total)
    print("Average Marks:", round(average, 2))

# Identify the top-performing student
top_index = totals.index(max(totals))

print("\nTOP PERFORMER")
print("Name:", students[top_index])
print("Total Marks:", totals[top_index])

# Calculate subject-wise averages
print("\nSUBJECT-WISE ANALYSIS")

for j in range(len(subjects)):
    subject_total = 0

    for i in range(len(students)):
        subject_total += marks[i][j]

    average = subject_total / len(students)

    print(subjects[j], "Average:", round(average, 2))

    if average < 70:
        print("Warning: Low average performance")
