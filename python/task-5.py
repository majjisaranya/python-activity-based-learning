# Smart Classroom Timetable Allocation

# Course details: (course_name, number_of_students)
courses = [
    ("Python", 40),
    ("Web Development", 30),
    ("Mathematics", 50),
    ("Communication", 25)
]

# Classroom details: (room_name, capacity)
rooms = [
    ("Room 101", 45),
    ("Room 102", 35),
    ("Room 103", 60)
]

# Available periods
periods = ["9 AM", "10 AM", "11 AM"]

# Timetable: (course, room, period)
timetable = [
    ("Python", "Room 101", "9 AM"),
    ("Web Development", "Room 102", "9 AM"),
    ("Mathematics", "Room 103", "10 AM"),
    ("Communication", "Room 101", "11 AM")
]

print("SMART CLASSROOM TIMETABLE")
print("-------------------------")

# Check classroom capacity
print("\nCLASSROOM CAPACITY CHECK")

for course, students in courses:
    allocated = False

    for room, capacity in rooms:
        if capacity >= students:
            print(course, "can fit in", room)
            allocated = True
            break

    if not allocated:
        print(course, "cannot fit in any classroom")

# Detect clashes
print("\nTIMETABLE CLASH CHECK")

clashes = False

for i in range(len(timetable)):
    for j in range(i + 1, len(timetable)):
        course1, room1, period1 = timetable[i]
        course2, room2, period2 = timetable[j]

        # Two courses cannot use the same room at the same time
        if room1 == room2 and period1 == period2:
            print("Room clash:", course1, "and", course2)
            clashes = True

        # A course cannot be scheduled more than once in the same period
        if course1 == course2 and period1 == period2:
            print("Course clash:", course1)
            clashes = True

if not clashes:
    print("No timetable clashes found")

# Check whether all courses are scheduled
print("\nCOURSE ALLOCATION CHECK")

scheduled_courses = [entry[0] for entry in timetable]

for course, students in courses:
    if course in scheduled_courses:
        print(course, "is scheduled")
    else:
        print(course, "is not scheduled")

if len(set(scheduled_courses)) == len(courses):
    print("All courses are accommodated")
else:
    print("Some courses are not accommodated")