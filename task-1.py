# University Scholarship Allocation System

students = []

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nEnter details of Student", i + 1)

    name = input("Enter student name: ")
    marks = float(input("Enter aggregate marks (%): "))
    attendance = float(input("Enter attendance (%): "))
    income = float(input("Enter annual family income (Rs): "))

    subject1 = float(input("Enter Subject 1 marks (%): "))
    subject2 = float(input("Enter Subject 2 marks (%): "))

    # Eligibility conditions
    if (marks >= 75 and
        subject1 >= 60 and
        subject2 >= 60 and
        attendance >= 75 and
        income <= 300000):

        students.append((name, marks, attendance, income))

        print("Eligible for scholarship")
    else:
        print("Not eligible for scholarship")


# Rank eligible students
students.sort(key=lambda student: student[1], reverse=True)

print("\n========== SCHOLARSHIP RANK LIST ==========")

if len(students) == 0:
    print("No students are eligible for scholarship.")
else:
    rank = 1

    for student in students:
        name, marks, attendance, income = student

        print("\nRank:", rank)
        print("Student Name:", name)
        print("Aggregate Marks:", marks)
        print("Attendance:", attendance, "%")
        print("Family Income: Rs.", income)

        rank += 1

print("\nScholarship allocation process completed.")